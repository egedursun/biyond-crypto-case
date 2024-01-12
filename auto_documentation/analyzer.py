from datetime import datetime

import dotenv

from auto_documentation.builder.builder_processor import build_input
from auto_documentation.gpt_client.GPTClient import GPTClient
from auto_documentation.reader.reader_processor import read_instructions, read_code_repository
import tiktoken

# load the .env file
dotenv.load_dotenv(dotenv.find_dotenv())
config = dotenv.dotenv_values()


def generate_report():
    instructions_path = "financial_reporter.txt"
    code_repository_path = "strategy"
    requirement_specification_path = "financial_reporter.txt"
    run_analysis(i=instructions_path, r=code_repository_path, s=requirement_specification_path)


def run_analysis(i, r, s):
    print("\n\n========================================")
    print("  GENERATOR/EMULATOR  ")
    print("========================================")
    print("")
    print("It is intended to be used for testing and development purposes.")
    print("")
    print("========================================")
    instructions = read_instructions(i)
    code_repository = read_code_repository(r)
    try:
        ct = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        with open(f"auto_documentation/transcribed_repos/transcribed_repo_{ct}.txt", "w") as f:
            f.write(code_repository)
    except Exception as e:
        print(e)
    requirement_specification = read_instructions(s)
    input_query = build_input(instructions, code_repository, requirement_specification)
    encoding = tiktoken.get_encoding("cl100k_base")
    num_tokens = len(encoding.encode(input_query))
    print("========================================")
    print(f"Number of tokens: {(num_tokens // 1000) + 4}K tokens.")
    print(f"Approximate Cost: ${((num_tokens // 1000) * 0.01) + (4.096 * 0.03)}.")
    print("========================================")
    # send the query to the client
    client = GPTClient(api_key=config["OPENAI_API_KEY"])
    result = client.get_response(input_query, "N/A")
    try:
        ct = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        with open(f"auto_documentation/generated_reports/report_{ct}.txt", "w") as f:
            f.write(result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    run_analysis("auto_documentation/instruction_files/financial_reporter.txt", "strategy",
                 "auto_documentation/requirement_specifications/financial_reporter.txt")

