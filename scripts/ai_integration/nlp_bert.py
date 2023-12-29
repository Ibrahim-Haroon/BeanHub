from transformers import AutoModel
from os import path


def ner_transformer(input_string: str = None):
    transformer_file_path = path.join(path.dirname(path.realpath(__file__)), "../..", "other/genai_models")

    model = AutoModel.from_pretrained(transformer_file_path)

    prediction, _ = model.predict([input_string])

    print(type(prediction))


if __name__ == "__main__":
    ner_transformer()
