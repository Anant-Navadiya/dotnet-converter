import os
from helpers import kebab_to_title, set_content

# Define source and destination folders
SOURCE_FOLDER = "./src/"
DESTINATION_FOLDER = "./dist/"

# Target file extensions
NEW_EXTENSION = "cshtml"
ADDITIONAL_EXTENSION = "cs"

# Flag to determine whether to add additional extension files
NEED_ADDITIONAL_EXTENSION = True

# Application name for namespace generation
APP_NAME = "Highdmin"


def process_file_name(file_name):
    """Processes the file name to extract folder and model names."""
    pre, ext = os.path.splitext(file_name)
    split_name = pre.split('-')

    folder_name = split_name[0].capitalize()
    model_name = (split_name[1].capitalize() + 'Model') if len(split_name) > 1 else 'IndexModel'

    return pre, folder_name, model_name


def add_additional_extension_files():
    """
    Creates additional files with an extra extension in the destination folder.
    The content of these files is generated using `set_content()`.
    """
    os.makedirs(DESTINATION_FOLDER, exist_ok=True)

    for file_name in os.listdir(SOURCE_FOLDER):
        pre, folder_name, model_name = process_file_name(file_name)
        new_file_name = f"{kebab_to_title(pre)}.{NEW_EXTENSION}.{ADDITIONAL_EXTENSION}"
        content = set_content(APP_NAME, folder_name, model_name)

        file_path = os.path.join(DESTINATION_FOLDER, new_file_name)

        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
            print(f"Created: {file_path}")
        except IOError as e:
            print(f"Error writing {file_path}: {e}")


def rename_and_move_files():
    """
    Iterates over files in SOURCE_FOLDER, renames them to PascalCase,
    changes their extension, adds content, and moves them to DESTINATION_FOLDER.
    """
    os.makedirs(DESTINATION_FOLDER, exist_ok=True)

    if NEED_ADDITIONAL_EXTENSION:
        add_additional_extension_files()

    for file_name in os.listdir(SOURCE_FOLDER):
        pre, folder_name, model_name = process_file_name(file_name)

        old_path = os.path.join(SOURCE_FOLDER, file_name)
        new_file_name = f"{kebab_to_title(pre)}.{NEW_EXTENSION}"
        new_path = os.path.join(DESTINATION_FOLDER, new_file_name)

        new_line = f"""@page "/{pre}"\n@model {APP_NAME}.Pages.{folder_name}.{model_name}\n"""

        try:
            # Read the file content
            with open(old_path, "r", encoding="utf-8", errors="ignore") as file:
                lines = file.readlines()

            # Insert new content at the beginning
            lines.insert(0, new_line)

            # Write to the new file in the destination folder
            with open(new_path, "w", encoding="utf-8") as file:
                file.writelines(lines)

            print(f"Processed: {old_path} -> {new_path}")

        except IOError as e:
            print(f"Error processing {old_path}: {e}")

rename_and_move_files()
