from openai import OpenAI
import sys
from tqdm import tqdm


def openai_api(prompt: str, api_key: str = None, model_behavior: str = None) -> str:
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
            model="gpt-4-1106-preview",
        )
    else:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-4-1106-preview",
        )

    return response.choices[0].message.content


def main(prompts: list[str]) -> int:
    with open("/Users/ibrahimharoon/Python/BeanHub/other/api_key") as api_key:
        key = api_key.readline().strip()

    for prompt in tqdm(prompts):
        prompt = prompt.strip()

        response = openai_api(prompt, key)

        print("question: " + prompt + " response: " + response)

    return 0


if __name__ == "__main__":
    sys.stdin = open("../IO/input.txt", 'r')
    sys.stdout = open("../IO/output.txt", 'w')

    istream = []

    for line in sys.stdin:
        istream.append(line)

    main(istream)
