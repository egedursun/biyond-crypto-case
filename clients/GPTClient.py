import dotenv
import openai

# Initialize dotenv
dotenv.load_dotenv(dotenv.find_dotenv())
config = dotenv.dotenv_values()


class GPTClient:
    class GPTAssistant:
        def __init__(self, instructions, model="gpt-4", max_tokens=200, temperature=0.5):
            self.instructions = instructions
            self.model = model
            self.max_tokens = max_tokens
            self.temperature = temperature

        def ask(self, question):
            response = openai.Completion.create(
                engine=self.model,
                temperature=0.5,
                max_tokens=200,
                messages=[question],  # TODO: add messages
            )
            answer = response.choices[0].text.strip()
            return answer

    def __init__(self):
        self.api_key = config['OPENAI_API_KEY']
        openai.api_key = self.api_key
        self.assistants = {}

    def build_assistant(self, name, instructions, model, max_tokens, temperature):
        assistant = self.GPTAssistant(instructions, model, max_tokens, temperature)
        self.assistants[name] = assistant

    def get_assistant(self, name):
        return self.assistants[name]
    

if __name__ == "__main__":
    pass
