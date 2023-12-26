from langchain.embeddings import OpenAIEmbeddings
from os import path


def embedding_api(api_key: str = None):
    embeddings = OpenAIEmbeddings(api_key=api_key)

    print(embeddings.embed_query('black coffee'))


def main() -> int:
    key_file_path = path.join(path.dirname(path.realpath(__file__)), "../..", "other", "api_key")
    with open(key_file_path) as api_key:
        key = api_key.readline().strip()


    embedding_api(key)

    return 0


if __name__ == "__main__":
    main()
