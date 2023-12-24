from openai import OpenAI
import sys
from tqdm import tqdm


class OpenAPI():
    def __init__(self, api_key: str = None):
        self.api_key = api_key

    def openai_caller(self, prompt: str, model_behavior: str = None) -> str:
        if self.api_key:
            client = OpenAI(api_key=self.api_key)
        else:
            client = OpenAI()

        if model_behavior:
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": model_behavior
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="gpt-3.5-turbo-1106",
            )
        else:
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="gpt-3.5-turbo-1106",
            )

        return chat_completion.choices[0].message.content


def main(prompts: list[str]) -> int:
    caller = OpenAPI()

    for prompt in tqdm(prompts):
        prompt = prompt.strip()

        response = caller.openai_caller(prompt)

        print(prompt + " " + response)

    return 0


if __name__ == "__main__":
    sys.stdin = open("IO/input.txt", 'r')
    sys.stdout = open("IO/output.txt", 'w')

    istream = []

    for line in sys.stdin:
        istream.append(line)

    main(istream)
