import os
from helpers import set_content, process_file_name, create_controller_file

SOURCE_FOLDER = "./src/"
DESTINATION_FOLDER = "./dist/"
NEW_EXTENSION = "cshtml"
ADDITIONAL_EXTENSION = "cs"
KEYWORDS = ("@page", "@model")

def add_additional_extension_files(app_name):
    """Creates .cshtml.cs files for Core architecture."""
    for file_name in os.listdir(SOURCE_FOLDER):
        if not file_name.endswith(".html"):
            continue

        pre, folder_name, file_base_name, model_name = process_file_name(file_name)
        os.makedirs(os.path.join(DESTINATION_FOLDER, folder_name), exist_ok=True)

        new_file_name = f"{file_base_name}.{NEW_EXTENSION}.{ADDITIONAL_EXTENSION}"
        content = set_content(app_name, folder_name, model_name)
        file_path = os.path.join(DESTINATION_FOLDER, folder_name, new_file_name)

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Created: {file_path}")
        except IOError as e:
            print(f"Error writing {file_path}: {e}")

def create_controllers(app_name):
    """Generates controller files based on folders and .cshtml files."""
    controllers_path = os.path.join(DESTINATION_FOLDER, "Controllers")
    os.makedirs(controllers_path, exist_ok=True)

    for folder_name in os.listdir(SOURCE_FOLDER):
        folder_path = os.path.join(SOURCE_FOLDER, folder_name)
        if not os.path.isdir(folder_path):
            continue

        actions = []
        for file in os.listdir(folder_path):
            if file.endswith(".cshtml") and not file.endswith(".cshtml.cs"):
                action_name = os.path.splitext(file)[0]
                actions.append(action_name)

        if actions:
            controller_file_path = os.path.join(controllers_path, f"{folder_name}Controller.cs")
            create_controller_file(controller_file_path, folder_name, actions, app_name)

def rename_and_move_files():
    """Main logic for converting HTML -> Core and Core -> MVC."""
    architecture = input('Enter architecture (Core/MVC): ').lower()

    is_core = architecture == 'core'
    is_mvc = False

    if architecture == 'mvc':
        is_valid_mvc = input("Have you converted to Core first? (yes/no): ").lower()
        if is_valid_mvc == 'no':
            print("Can't convert to MVC. Convert it to Core first.")
            return
        else:
            is_mvc = True

    app_name = input('Enter app name: ').capitalize()

    if is_core:
        need_sub_title = input("Do you want to add SubTitle? (yes/no): ").lower()
        add_additional_extension_files(app_name)

        for file_name in os.listdir(SOURCE_FOLDER):
            if not file_name.endswith(".html"):
                continue

            old_path = os.path.join(SOURCE_FOLDER, file_name)
            pre, folder_name, file_base_name, model_name = process_file_name(file_name)
            output_folder = os.path.join(DESTINATION_FOLDER, folder_name)
            os.makedirs(output_folder, exist_ok=True)

            new_file_name = f"{file_base_name}.{NEW_EXTENSION}"
            new_path = os.path.join(output_folder, new_file_name)

            new_line = f"""@page "/{pre}"
@model {app_name}.Pages.{folder_name}.{model_name}

@{{
    ViewBag.Title = "{file_base_name}";
    {f'ViewBag.SubTitle = "{folder_name}";' if (need_sub_title == 'yes') else ''}
}}

@section styles
{{
}}

@section scripts
{{
}}

"""

            try:
                with open(old_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                with open(new_path, "w", encoding="utf-8") as f:
                    f.write(new_line + content)

                print(f"Generated Core: {old_path} -> {new_path}")
            except IOError as e:
                print(f"Error processing {old_path}: {e}")

    elif is_mvc:
        for root, _, files in os.walk(SOURCE_FOLDER):
            for file in files:
                if file.endswith(".cshtml") and not file.endswith(".cshtml.cs"):
                    src_path = os.path.join(root, file)
                    relative_path = os.path.relpath(src_path, SOURCE_FOLDER)
                    dest_path = os.path.join(DESTINATION_FOLDER, relative_path)

                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

                    try:
                        with open(src_path, "r", encoding="utf-8", errors="ignore") as f:
                            lines = f.readlines()

                        filtered_lines = [
                            line for line in lines
                            if not any(line.strip().startswith(keyword) for keyword in KEYWORDS)
                        ]

                        with open(dest_path, "w", encoding="utf-8") as f:
                            f.writelines(filtered_lines)

                        print(f"Converted to MVC: {src_path} -> {dest_path}")
                    except IOError as e:
                        print(f"Error processing {src_path}: {e}")

        create_controllers(app_name)

rename_and_move_files()
