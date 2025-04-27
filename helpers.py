import os

def process_file_name(file_name):
    """Extract folder, file, and model names from kebab-case filename."""
    pre, _ = os.path.splitext(file_name)
    split_name = pre.split('-')
    folder_name = split_name[0].capitalize()

    if len(split_name) > 1:
        # Join all parts after the first part and capitalize each one
        file_name = "".join(part.capitalize() for part in split_name[1:])
    else:
        file_name = "Index"

    model_name = f"{file_name}Model"
    return pre, folder_name, file_name, model_name


def set_content(app_name, folder_name, model_name):
    """Generates default content for .cshtml.cs files."""
    return f"""using Microsoft.AspNetCore.Mvc.RazorPages;

namespace {app_name}.Pages.{folder_name}
{{
    public class {model_name} : PageModel
    {{
        public void OnGet() {{ }}
    }}
}}
"""

def create_controller_file(path, folder_name, actions, app_name):
    """Creates a controller file with actions."""
    lines = [
        "using Microsoft.AspNetCore.Mvc;\n",
        f"\nnamespace {app_name}.Controllers\n{{\n",
        f"    public class {folder_name}Controller : Controller\n    {{\n"
    ]
    for action in actions:
        lines.append(f"        public IActionResult {action}() => View();\n")
    lines.append("    }\n}")

    try:
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print(f"Created controller: {path}")
    except IOError as e:
        print(f"Error writing controller file: {e}")
