import os

import fire
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def ask(question: str):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{question}",
            }
        ],
        model="gpt-3.5-turbo",
    )
    print("#####")
    print(chat_completion.choices[0].message.content)
    print("#####")


if __name__ == "__main__":
    fire.Fire(ask)
