def kebab_to_title(text):
    """
    Converts a kebab-case string to PascalCase.
    """
    return "".join(word.capitalize() for word in text.split("-"))


def set_content(app_name, file_name):
    """
    Generates the C# Razor PageModel class content for the given file name.
    """
    return f"""using Microsoft.AspNetCore.Mvc.RazorPages;

namespace {app_name}.Pages.{file_name}
{{
    public class {file_name}Model : PageModel
    {{
        public void OnGet()
        {{
        }}
    }}
}}
    """
