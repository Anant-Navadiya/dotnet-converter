def kebab_to_title(text):
    """
    Converts a kebab-case string to PascalCase.
    """
    return "".join(word.capitalize() for word in text.split("-"))


def set_content(app_name, folder_name, model_name):
    """
    Generates the C# Razor PageModel class content for the given file name.
    """
    return f"""using Microsoft.AspNetCore.Mvc.RazorPages;

namespace {app_name}.Pages.{folder_name}
{{
    public class {model_name}: PageModel
    {{
        public void OnGet()
        {{
        }}
    }}
}}
    """
