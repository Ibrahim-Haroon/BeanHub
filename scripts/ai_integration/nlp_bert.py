from transformers import AutoModel
from os import path
from word2number import w2n


def ner_transformer(input_string: str = None) -> list:
    transformer_file_path = path.join(path.dirname(path.realpath(__file__)), "../..", "other/genai_models/outputs")

    model = AutoModel.from_pretrained(transformer_file_path)

    prediction, _ = model.predict([input_string])

    return prediction


def format_ner(ner_prediction: list):
    order = []
    formatted_order = []

    for prediction in ner_prediction:
        for entity_dict in prediction:
            for word, tag in entity_dict.items():
                if tag != 'O':
                    order.append(entity_dict)

    temp = None
    for pair in order:
        for word, tag in pair.items():
            if tag == 'B_QUANTITY':
                temp = word
            elif tag != 'B_QUANTITY' and temp is not None:
                formatted_order.append(pair)
                formatted_order.append({temp: 'I_QUANTITY'})
                temp = None
            else:
                formatted_order.append(pair)

    res = []
    for pair in formatted_order:
        for word, tag in pair.items():
            res.append([word, tag])

    res1 = []
    for i in range(len(res)):
        if res[i][1] != 'I_QUANTITY':
            res1.append(res[i][0])
            if i == len(res)-1:
                res1.append(1)
        elif res[i][1] == 'I_QUANTITY' and isinstance(res[i][0], str):
                res1.append(w2n.word_to_num(res[i][0]))


    print(res1)


if __name__ == "__main__":
    # pred = [[{'if': 'O'}, {'you': 'O'}, {'have': 'O'}, {'any': 'O'}, {'more': 'O'}, {'cinnamon rolls': 'B_BAKERY_ITEM'},
    #          {'left': 'O'}, {'I’ll': 'O'}, {'take': 'O'}, {'one': 'I_QUANTITY'}, {'and': 'O'}, {'then': 'O'},
    #          {'also': 'O'}, {'just': 'O'}, {'a': 'O'}, {'black coffee': 'B_COFFEE_TYPE'}]]

    pred = [[{'if': 'O'}, {'you': 'O'}, {'have': 'O'}, {'one': 'B_QUANTITY'}, {'cinnamon roll': 'I_BAKERY_ITEM'},
             {'left': 'O'}, {'I’ll': 'O'}, {'take': 'O'}, {'it': 'O'}, {'and': 'O'}, {'then': 'O'},
             {'also': 'O'}, {'just': 'O'}, {'a': 'O'}, {'black coffee': 'B_COFFEE_TYPE'}]]
    res = format_ner(pred)

    print(res)