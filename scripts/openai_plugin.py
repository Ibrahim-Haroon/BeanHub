from openai import OpenAI
import sys
from tqdm import tqdm


def openai_api(prompt: str, model_behavior: str = None, api_key: str = None) -> str:
    if api_key:
        client = OpenAI(api_key=api_key)
    else:
        client = OpenAI()

    if model_behavior:
        response = client.chat.completions.create(
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
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo-1106",
        )

    return response.choices[0].message.content


def main(prompts: list[str]) -> int:
    for prompt in tqdm(prompts):
        prompt = prompt.strip()

        response = openai_api(prompt)

        print(prompt + " " + response)

    return 0


if __name__ == "__main__":
    sys.stdin = open("IO/input.txt", 'r')
    sys.stdout = open("IO/output.txt", 'w')

    istream = []

    for line in sys.stdin:
        istream.append(line)

    main(istream)
