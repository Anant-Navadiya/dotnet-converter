# File Extension Changer

This script changes the file extensions of files from a specified source folder and moves them to a destination folder. The extension of each file is updated to a new extension defined in the script.

## Features:
- **Batch rename**: Changes the extension of all files in the source folder.
- **File movement**: Moves renamed files to the destination folder.
- **Customizable extension**: Easily modify the target extension.

## Requirements:
- Python 3.x
- No external libraries required

## Usage

1. **Clone the repository**:
   ```
   git clone https://github.com/Anant-Navadiya/dotnet-file-extention-renamer.git
   ```
   
2. **Modify the script:**

    -Set SOURCE_FOLDER to the path of the folder containing files to rename.

    -Set DESTINATION_FOLDER to the path where you want to move the renamed files.

    -Set NEW_EXTENSION to the extension you want to apply to the files (Do not add a dot before the extension).

   -Set NEED_ADDITIONAL_EXTENSION to the True/False if you want/do not want any additional file with extension (If True this will generate new files with some content from the function set_content in helpers.py file).

   -Set ADDITIONAL_EXTENSION to the extension you want to apply to the additional files (Do not add a dot before the extension).

   -Set APP_NAME to the name of your app.

3. **Run the script:**
    ```
    python dotnet-file-extension-renamer.py
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
├── FileOne.cshtml
├── FileOne.cshtml.cs
├── FileTwo.cshtml
├── FileTwo.cshtml.cs
├── FileThree.cshtml
└── FileThree.cshtml.cs
```