# HTML to ASP.NET Core/MVC Converter

This Python script automates the process of converting static `.html` files into ASP.NET Core Razor Pages or MVC Views. It also supports generating `.cshtml.cs` code-behind files and MVC `Controller` classes based on the folder structure and file names.

---

## 🚀 Features

- Converts `.html` files to `.cshtml` Razor Pages or MVC Views.
- Converts kebab-case filenames into PascalCase for better C# naming conventions.
- Optionally generates `.cshtml.cs` files for Razor Pages.
- Automatically strips `@page` and `@model` when converting to MVC.
- Automatically generates MVC `Controller` files with actions for each view.
- Handles Unicode/encoding errors gracefully.
- Uses only built-in Python libraries (no installation required).

---

## 📦 Requirements

- Python 3.x  
- No external libraries needed (uses only `os`, `shutil`, etc.)

---

## 🛠️ Usage

### Clone the Repository

```
git clone https://github.com/Anant-Navadiya/dotnet-converter.git
cd dotnet-converter
```
---

### 🔧 HTML to ASP.NET Core (Razor Pages)

1. **Add your HTML files**  
   - Place all your `.html` files into the `src/` folder.  
   - File names should follow this format:

        ```
        foldername-filename.html
        ```

        **Examples:**
        - `blog-index.html`
        - `shop-product.html`

2. **Run the script**

   ```
   python convert.py
   # or
   python3 convert.py
   ```

3. **Follow the prompts**
   - Enter architecture: `core`
   - Enter your app name (used for namespace/model)
   - Choose whether to include `SubTitle`

---

### 🔁 Core to MVC Conversion

1. **Move Core output to `src/`**  
   - Take the core-converted files (from `dist/`) and place them into the `src/` folder.

2. **Run the script**

   ```
   python convert.py
   # or
   python3 convert.py
   ```

3. **Follow the prompts**
   - Enter architecture: `mvc`
   - Confirm that core conversion is done.


---

## 📄 Example

### Core Input (`src/`):

```
src
├── blog-index.html
├── blog-left.html
└── blog-right.html
```

### Core Output (`dist/`):

```
dist
└── Blog
    ├── Index.cshtml
    ├── Index.cshtml.cs
    ├── Left.cshtml
    ├── Left.cshtml.cs
    ├── Right.cshtml
    └── Right.cshtml.cs
```
### MVC Input (`src/`):

```
src
└── Blog
    ├── Index.cshtml
    ├── Index.cshtml.cs
    ├── Left.cshtml
    ├── Left.cshtml.cs
    ├── Right.cshtml
    └── Right.cshtml.cs
```
### MVC Output (`dist/`):

```
dist
├── Blog
│   ├── Index.cshtml
│   ├── Left.cshtml
│   └── Right.cshtml
└── Controllers
    └── BlogController.cs
```

Generated BlogController:

```
using Microsoft.AspNetCore.Mvc;

namespace APP_NAME.Controllers
{
    public class BlogController : Controller
    {
        public IActionResult Index() => View();
        public IActionResult Left() => View();
        public IActionResult Right() => View();
    }
}
```

---

## 📌 Notes

- MVC conversion will only copy `.cshtml` files (not `.cshtml.cs`) and remove `@page` and `@model` lines.
- Controller actions are auto-generated based on `.cshtml` file names.
- This script expects proper naming structure to determine folders and view names correctly.

---

## 🙌 Contribution

Pull requests, issues, and feature suggestions are welcome. Feel free to fork and improve it!

---

## 📄 License

MIT License – free to use and modify.