import openai
import dotenv


# load the .env file
dotenv.load_dotenv(dotenv.find_dotenv())
config = dotenv.dotenv_values()


class GPTClient:

    def __init__(self, api_key):
        self.api_key = api_key

        # create the client connection
        self.connection = openai.Client(api_key=self.api_key)

    def get_response(self, input_query: str, additional_note: str) -> str:
        input_query += "\n --- HERE IS ADDITIONAL NOTE FROM THE USER: \n" + additional_note
        agent_response = self.connection.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": """
                    You are an assistant tasked with generating take home case studies for job interviews. You are given:
                    - A textualized version of a code repository:
                        - A code repository of the company that's hiring. This is shared for you to determine a great
                        report for the contents of the quantiative methods repository. However, you need to make sure 
                        that the report is not shallow, and make sure that it includes all the essential information
                        about the repository, approaches, methodologies, advantages, disadvantages and performance of
                        the strategies.
                    - A requirement specification file containing the requirements for the case study:
                        - A requirement specification file containing the requirements for report. This is
                        shared for you to build a great report for this quantitative finance experiment. However, 
                         need to make sure that the report is not shallow, and make sure that it includes all the
                            essential information about the repository, approaches, methodologies, advantages,
                            disadvantages and performance of the strategies.
                    - An instruction document containing the requirements of the report in a general sense:
                        - An instruction document containing the requirements of the report in a general sense. This is
                        shared for you to build a great report for this quantitative finance experiment.
                    """},
                {"role": "user", "content": input_query},
            ],
            temperature=0.9,
            max_tokens=4096,
        )
        return agent_response.choices[0].message.content


if __name__ == "__main__":
    client = GPTClient(api_key=config["OPENAI_API_KEY"])

    # send a query to the client
    test_result = client.get_response("I am working on an interview for a job position. ", "something")
    print(test_result)

