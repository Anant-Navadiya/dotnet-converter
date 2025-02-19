import os
from helpers import kebab_to_title, set_content

# Define source and destination folders
SOURCE_FOLDER = "./src/"
DESTINATION_FOLDER = "./dist/"

# Target file extension
NEW_EXTENSION = "cshtml"

# Flag to determine whether to add additional extension files
NEED_ADDITIONAL_EXTENSION = True
ADDITIONAL_EXTENSION = "cs"

# Application name for namespace generation
APP_NAME = "Hyper"


def add_additional_extension_files():
    """
    Creates additional files with an extra extension in the destination folder.
    The content of these files is generated using `get_content()`.
    """
    additional_files = []

    for file_name in os.listdir(SOURCE_FOLDER):
        pre, ext = os.path.splitext(file_name)

        new_file_name = kebab_to_title(pre) + '.' + NEW_EXTENSION

        additional_files.append(new_file_name + '.' + ADDITIONAL_EXTENSION)

    for file_name in additional_files:
        prefix = file_name.split(".", 1)[0]

        content = set_content(APP_NAME, prefix)

        file_path = os.path.join(DESTINATION_FOLDER, file_name)
        with open(file_path, "w") as file:
            file.write(content)


def rename_and_move_files():
    """
    Iterates over files in SOURCE_FOLDER, renames them to PascalCase,
    changes their extension, and moves them to DESTINATION_FOLDER.
    """
    os.makedirs(DESTINATION_FOLDER, exist_ok=True)

    if NEED_ADDITIONAL_EXTENSION:
        add_additional_extension_files()

    for file_name in os.listdir(SOURCE_FOLDER):
        pre, ext = os.path.splitext(file_name)

        old_path = os.path.join(SOURCE_FOLDER, file_name)
        new_path = os.path.join(DESTINATION_FOLDER, kebab_to_title(pre) + '.' + NEW_EXTENSION)

        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} -> {new_path}")


rename_and_move_files()
