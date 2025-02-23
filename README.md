# File Extension Changer

This script automates the conversion of files from the source folder, renaming them to PascalCase, updating their
extension to .cshtml, and optionally generating additional .cs files. The processed files are moved to the another folder
while inserting specific content based on the file structure.

## Features:

- Converts filenames from kebab-case to PascalCase.
- Changes file extensions to .cshtml.
- Optionally generates additional .cs files.
- Inserts specific content based on the application structure.
- Handles encoding issues to prevent Unicode errors.

## Requirements:

- Python 3.x
- No external libraries required

## Usage

1. **Clone the repository**:
   ```
   git clone https://github.com/Anant-Navadiya/dotnet-converter.git
   ```

2. **Modify the script:**

   -Set SOURCE_FOLDER to the path of the source folder.

   -Set DESTINATION_FOLDER to the path of the destination folder.

   -Set NEW_EXTENSION to the extension you want to apply to the files (Do not add a dot before the extension).

   -Set NEED_ADDITIONAL_EXTENSION to the True/False if you want/do not want any additional file with extension (If True
   this will generate new files with some content from the function set_content in helpers.py file).

   -Set ADDITIONAL_EXTENSION to the extension you want to apply to the additional files (Do not add a dot before the
   extension).

   -Set APP_NAME to the name of your app.

3. **Run the script:**
    ```
    python converter.py
    ```

## Example

```
SOURCE_FOLDER = "./src/"
DESTINATION_FOLDER = "./dist/"
NEW_EXTENSION = "cshtml"

NEED_ADDITIONAL_EXTENSION = True
ADDITIONAL_EXTENSION = "cs"

APP_NAME = "Hyper"
```

Assume you have the following files in the src/ folder:

```
src/
├── file-one.html
├── file-two.html
└── file-three.html
```

after running the script, the files in the dist/ folder will be:

```
dist/
└── File
    ├── One.cshtml
    ├── One.cshtml.cs
    ├── Two.cshtml
    ├── Two.cshtml.cs
    ├── Three.cshtml
    └── Three.cshtml.cs
```