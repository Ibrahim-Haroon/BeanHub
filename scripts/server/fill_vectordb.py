from langchain.vectorstores.pgvector import PGVector
from scripts.ai_integration.openai_embeddings_api import *


def connection_string() -> str:
    connection_string_file_path = path.join(path.dirname(path.realpath(__file__)), "../..", "other",
                                            "connection_string")
    with open(connection_string_file_path) as connection_str:
        connection = connection_str.readline().strip()

    return connection


def fill_database(key: str = None):
    menu = parse_menu_csv()
    vectors, embeddings = embedding_api(menu, key)


    db = PGVector.from_embeddings(text_embeddings=vectors, embedding=embeddings, metadatas=menu, collection_name="coffee_types", connection_string=connection_string())


def main() -> int:
    key_file_path = path.join(path.dirname(path.realpath(__file__)), "../..", "other", "api_key")
    with open(key_file_path) as api_key:
        key = api_key.readline().strip()

    fill_database(key)

    return 0


if __name__ == "__main__":
    main()
