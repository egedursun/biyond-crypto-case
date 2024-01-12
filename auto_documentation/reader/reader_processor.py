from auto_documentation.transcriber.transcriber_processor import transcribe_code_repository


def read_instructions(filename: str) -> str or None:
    complete_filename = "auto_documentation/instruction_files/" + filename
    instructions = None
    try:
        with open(complete_filename, "r") as file:
            instructions = file.read()
    except FileNotFoundError as e:
        print(f"Instruction file ({complete_filename}) is not found. "
              f"Please check the file name and try again.")
    return instructions


def read_code_repository(filename: str) -> str or None:
    complete_filename = filename
    content = transcribe_code_repository(complete_filename)
    return content


def read_requirement_specifications(filename: str) -> str or None:
    complete_filename = "auto_documentation/requirement_specifications/" + filename
    requirements = None
    try:
        with open(complete_filename, "r") as file:
            requirements = file.read()
    except FileNotFoundError as e:
        print(f"Requirement specification file ({complete_filename}) is not found. "
              f"Please check the file name and try again.")
    return requirements


def read_report(filename: str) -> str or None:
    complete_filename = "auto_documentation/generated_reports/" + filename
    reports = None
    try:
        with open(complete_filename, "r") as file:
            reports = file.read()
    except FileNotFoundError as e:
        print(f"Report file ({complete_filename}) is not found. "
              f"Please check the file name and try again.")
    return reports


if __name__ == "__main__":
    pass
