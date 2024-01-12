import os

TRANSCRIBED_FORMATS = (
    "py", "txt",
)

EXCLUDE_FILES = (
    ##  placeholder
)

EXCLUDE_PREFIXES = (
    ##  placeholder
)

EXCLUDE_SUFFIXES = (
    ##  placeholder
)


def transcribe_code_repository(filename: str) -> str or None:
    main_content = ""

    try:

        # iterate through all files of the code repository
        for root, dirs, files in os.walk(filename):
            for file in files:
                if file.startswith(EXCLUDE_PREFIXES):
                    continue
                if file.endswith(EXCLUDE_SUFFIXES):
                    continue
                # check if the file is a python file
                if file.endswith(TRANSCRIBED_FORMATS) and file not in EXCLUDE_FILES:
                    # open the file
                    with open(os.path.join(root, file), "r") as f:

                        # add the headers and metadata
                        main_content += "========================================"
                        main_content += f"METADATA"
                        main_content += f"Path: {os.path.join(root, file)}\n"
                        main_content += f"File: {f.name}\n"
                        main_content += f"Size: {os.path.getsize(f.name)}\n"
                        main_content += f"Last modified: {os.path.getmtime(f.name)}\n"
                        main_content += f"Last accessed: {os.path.getatime(f.name)}\n"
                        main_content += f"Created: {os.path.getctime(f.name)}\n"
                        main_content += f"Owner: {os.stat(f.name).st_uid}\n"
                        main_content += f"Group: {os.stat(f.name).st_gid}\n"
                        main_content += f"Permissions: {os.stat(f.name).st_mode}\n"
                        main_content += f" --- At the start of each line, there is a number that represents " \
                                        f"the line number, which is separated from content with '|'.\n"
                        main_content += f"========================================\n"
                        main_content += f"<CONTENT START>\n"

                        # read the contents line by line
                        for line_number, line in enumerate(f.readlines()):
                            # add the line number at the start of the line
                            main_content += f"{line_number} | {line}"

                        main_content += f"<CONTENT END>\n\n"

                else:
                    # print(f"File {file} is not a supported format, skipping...")
                    continue

    except FileNotFoundError as e:
        print("File not found. Please check the file name and try again.")
        return None

    return main_content
