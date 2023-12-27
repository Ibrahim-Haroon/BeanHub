from langchain.embeddings import OpenAIEmbeddings
from os import path
import pandas as pd


def openai_embedding_api(text: str, api_key: str = None) -> []:
    """

    @rtype: list[list[float]], embeddings object
    @param text: str = contains item name and price
    @param api_key: auth method for OpenAI
    @return: vectors of each menu item to insert into vector_db
    """

    embeddings = OpenAIEmbeddings(api_key=api_key)

    return embeddings.embed_query(text)



def parse_menu_csv() -> list[str]:
    """

    @rtype: list[str]
    @return: str menu items packaged in a list
    """
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

        menu_items.append(str(item))

    return menu_items


def main(key_path: str) -> int:
    """

    @param key_path: api key for OpenAI
    @return: 0 for success
    """
    with open(key_path) as api_key:
        key = api_key.readline().strip()

    menu = parse_menu_csv()

    vectors = []

    for item in menu:
        vectors.append(openai_embedding_api(item, key))

    return 0


if __name__ == "__main__":
    key_file_path = path.join(path.dirname(path.realpath(__file__)), "../..", "other", "api_key")
    main(key_file_path)
