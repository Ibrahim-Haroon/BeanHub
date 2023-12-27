import boto3
import psycopg2
from pgvector.psycopg2 import register_vector
from aiohttp import ClientError
from scripts.ai_integration.openai_embeddings_api import *
import panda as pd


def get_secret():
    secret_file_path = connection_string_file_path = path.join(path.dirname(path.realpath(__file__)), "../..", "other", "aws-info.csv")

    df = pd.read_csv(secret_file_path)
    row = df.iloc[0]

    secret_name = row['secret_name']
    region_name = row['region_name']
    aws_access_key_id = row['aws_access_key_id']
    aws_secret_access_key = row['aws_secret_access_key']

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    return get_secret_value_response['SecretString']


def connection_string() -> str:
    """

    @rtype: str
    @return: connection string for PostgreSQL
    """
    db_info_file_path = connection_string_file_path = path.join(path.dirname(path.realpath(__file__)), "../..", "other", "database-info.csv")

    df = pd.read_csv(db_info_file_path)
    row = df.iloc[0]

    dsn = f"dbname={row['dbname']} user={row['user']} password={row['password']} host={row['host']} port={row['port']}"

    return dsn


def fill_database(data: list[dict], key: str = None) -> bool:
    get_secret()

    db_connection = psycopg2.connect(connection_string())
    db_connection.set_session(autocommit=True)

    cur = db_connection.cursor()
    cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
    register_vector(db_connection)
    cur.execute("DROP TABLE IF EXISTS products;")

    cur.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                item_name text,
                price double precision,
                embeddings vector(1536)
            );
        """)

    for item in data:
        cur.execute("""
            INSERT INTO products (item_name, price, embeddings)
            VALUES (%s, %s, %s);
        """, (item["MenuItem"]["itemName"], item["MenuItem"]["price"], openai_embedding_api(str(item), key)))

    cur.execute("""
            CREATE INDEX ON products
            USING ivfflat (embeddings) WITH (lists = 8);
        """)
    cur.execute("VACUUM ANALYZE products;")

    cur.close()
    db_connection.close()

    return True


def main() -> int:
    key_path = path.join(path.dirname(path.realpath(__file__)), "../..", "other", "api_key")
    with open(key_path) as api_key:
        key = api_key.readline().strip()

    menu = parse_menu_csv()
    fill_database(menu, key)

    return 0


if __name__ == "__main__":
    main()
