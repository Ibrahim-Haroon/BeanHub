import psycopg2
from pgvector.psycopg2 import register_vector
from scripts.ai_integration.openai_embeddings_api import *
from scripts.server.aws_secret import get_secret
from scripts.server.connection_string import connection_string
from other.red import inputRED


def fill_database(data: list[dict], key: str = None) -> bool:
    """

    @rtype: bool
    @param data: all the menu items which have to be embedded and inserted in DB
    @param key: key for OpenAI auth
    @return: true if successfully created and filled table
    """

    if (inputRED() != "YES"):
        return False
    else:
        if (str(input("Enter the passkey to confirm: ")) != "beanKnowsWhatBeanWants"):
            return False

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
