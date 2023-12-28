import psycopg2
from io import StringIO
from scripts.server.aws_secret import get_secret
from scripts.ai_integration.openai_embeddings_api import *
from scripts.server.connection_string import connection_string
from scripts.ai_integration.nlp_bard import nlp_bard
import numpy as np


def similarity_search(order: str, key: str = None, aws_csv_file: StringIO = None, database_csv_file: StringIO = None) -> object:
    formatted_string = nlp_bard(order)

    embedding = openai_embedding_api(formatted_string, key)


    get_secret(aws_csv_file if not None else None)
    db_connection = psycopg2.connect(connection_string(database_csv_file if not None else None))
    db_connection.set_session(autocommit=True)

    cur = db_connection.cursor()
    cur.execute(""" SELECTED id, item_name, price, embeddings
                    FROM products
                    ORDER BY embeddings <-> %s limit 3;""",
                (np.array(embedding),))
    results = cur.fetchall()

    cur.close()
    db_connection.close()

    return results, True


def main() -> int:
    key_path = path.join(path.dirname(path.realpath(__file__)), "../..", "other", "api_key")
    with open(key_path) as api_key:
        key = api_key.readline().strip()

    similarity_search(order="dummy", key=key)

    return 0


if __name__ == "__main__":
    main()