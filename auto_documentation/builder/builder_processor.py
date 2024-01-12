import random

import tiktoken


def build_input(instructions: str, repo_transcription: str, specifications: str) -> str:

    token_length = len(tiktoken.get_encoding("cl100k_base").encode(repo_transcription))
    print("========================================")
    print(f"Token length: {token_length}")
    if token_length > 120_000:
        repo_transcription = repo_transcription.replace("  ", " ")
        repo_transcription = repo_transcription.replace("   ", " ")
        repo_transcription = repo_transcription.replace("    ", " ")
        repo_transcription = repo_transcription.replace("\n\n", "\n")
        repo_transcription = repo_transcription.replace("\n\n\n", "\n")
        repo_transcription = repo_transcription.replace("\n\n\n\n", "\n")
        repo_transcription = repo_transcription.replace("========================================", " ")

        token_length = len(tiktoken.get_encoding("cl100k_base").encode(repo_transcription))
        if token_length > 135_000:
            while token_length > 120_000:
                chunk_size = 5000
                chunk_start = random.randint(0, len(repo_transcription) - chunk_size)
                chunk_end = chunk_start + chunk_size
                repo_transcription = repo_transcription[:chunk_start] + repo_transcription[chunk_end:]
                token_length = len(tiktoken.get_encoding("cl100k_base").encode(repo_transcription))

                print(f"Token length: {token_length}")

    # This function builds the input for the RAG Assistant.
    main_query = "INPUT QUERY: \n"
    main_query += "========================================\n"
    main_query += "INSTRUCTIONS: \n\n"
    main_query += instructions
    main_query += "\n\n========================================\n"
    main_query += "CODE REPOSITORY: \n\n"
    main_query += repo_transcription
    main_query += "\n\n========================================\n"
    main_query += "REQUIREMENT SPECIFICATIONS: \n\n"
    main_query += specifications
    main_query += "\n\n========================================\n"

    main_query += "IMPORTANT META INSTRUCTIONS FOR LLM ASSISTANT: \n"
    main_query += "========================================\n"
    main_query += "1. THIS ASSISTANT IS FOR THE PURPOSE OF GENERATING FINANCIAL REPORTS FOR REPOSITORIES INCLUDING" \
                  " QUANTITATIVE STRATEGIES. \n"
    main_query += "2. YOUR TASK IS TO GENERATE A REPORT FOR A REPOSITORY, INCLUDING A FINANCIAL STRATEGY. \n"
    main_query += "3. THE REPORT SHOULD REFLECT THE APPROACHES, METHODOLOGIES, ADVANTAGES, DISADVANTAGES AND PERFORMANCE " \
                  "OF THE STRATEGIES. \n"
    main_query += "4. MAKE SURE TO USE THE CODE REPOSITORY AND REQUIREMENT SPECIFICATIONS I SHARED. \n"
    main_query += "5. MAKE SURE TO USE THE INSTRUCTION DOCUMENT I SHARED TO DETERMINE A GREAT CASE STUDY FOR THE JOB " \
            "POSITION. \n"
    main_query += "========================================\n\n"

    return main_query
