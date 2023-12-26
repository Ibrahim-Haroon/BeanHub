from langchain.embeddings import OpenAIEmbeddings
from os import path
import pandas as pd


def embedding_api(texts: [str], api_key: str = None):
    vectors = []
    embeddings = OpenAIEmbeddings(api_key=api_key)

    for text in texts:
        vectors.append(embeddings.embed_query(text))

    return vectors


def parse_menu_csv():
    menu_items = []

    menu_file_path = path.join(path.dirname(path.realpath(__file__)), "../IO", "menu.csv")

    df = pd.read_csv(menu_file_path)

    for index, row in df.iterrows():
        item_name = row['item_name']
        price = row['price']

        item = {
            "MenuItem": {
                "itemName": item_name,
                "price": float(price)
            }
        }

        menu_items.append(item)

    return menu_items


def main() -> int:
    key_file_path = path.join(path.dirname(path.realpath(__file__)), "../..", "other", "api_key")
    with open(key_file_path) as api_key:
        key = api_key.readline().strip()


    menu = parse_menu_csv()
    print(menu[0])
    vectors = embedding_api(menu, key)
    print(len(vectors))

    return 0


if __name__ == "__main__":
    main()
