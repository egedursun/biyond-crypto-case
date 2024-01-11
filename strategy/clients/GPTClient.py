import contextlib
import io
import sys

import dotenv
import openai
from openai import OpenAI

dotenv.load_dotenv(dotenv.find_dotenv())
config = dotenv.dotenv_values()


class GPTClient:
    class GPTAssistant:
        def __init__(self, client, instructions, model="gpt-4", max_tokens=200, temperature=0.5):
            self.instructions = instructions
            self.model = model
            self.max_tokens = max_tokens
            self.temperature = temperature
            self.client = client

        def ask(self, question, **kwargs):
            message_list = [
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": question},
            ]
            for addition in kwargs:
                message_list.insert(1, {"role": "system", "content": kwargs[addition]})
            response = self.client.chat.completions.create(
                model=self.model,
                messages=message_list,
            )
            answer = response.choices[0].message.content
            return answer

    def __init__(self):
        self.api_key = config['OPENAI_API_KEY']
        self.client = OpenAI(api_key=self.api_key)
        self.assistants = {}

    def build_assistant(self, name, instructions, model, max_tokens, temperature):
        ast = self.GPTAssistant(self.client, instructions, model, max_tokens, temperature)
        self.assistants[name] = ast

    def get_assistant(self, name):
        return self.assistants[name]


if __name__ == "__main__":
    # test the GPTClient
    gpt_client = GPTClient()
    gpt_client.build_assistant(name="test",
                               instructions=
                               """
                               You are a helpful assistant.
                               """,
                               model="gpt-4",
                               max_tokens=500,
                               temperature=0.0)
    assistant = gpt_client.get_assistant(name="test")
    # print(assistant.ask("What is your name?"))
    # print(assistant.ask("What is 2 + 2?"))
    # print(assistant.ask("Do androids dream of electric sheep?"))
    print(assistant.ask("What is the meaning of life?", addt="(The answer is 42.)"))

