# Ruff Configurations

!!! TIP
    Official documentation for Ruff is available at [https://docs.astral.sh/ruff](https://docs.astral.sh/ruff)

The Ruff formatter is an extremely fast Python code formatter designed as a drop-in replacement for Black, available as part of the ruff CLI via ruff format.

<div align="center">
    <img src="https://user-images.githubusercontent.com/1309177/232603516-4fb4892d-585c-4b20-b810-3db9161831e4.svg#only-light">
    <img src="https://user-images.githubusercontent.com/1309177/232603514-c95e9b0f-6b31-43de-9a80-9e844173fd6a.svg#only-dark">
</div>
<p align="center">
  <i>Linting the CPython codebase from scratch.</i>
</p>


## ruff.toml
!!! WARNING
    Note that when using ruff as a formatter, [it is officially recommended](https://docs.astral.sh/ruff/formatter/#format-suppression) to avoid the following lint rule, which is not the default in ruff.
    They are set as default in this repository.

=== "ruff.toml"
    ```{.toml hl_lines=42-57}
    # Exclude a variety of commonly ignored directories.
    exclude = [
        ".bzr",
        ".direnv",
        ".eggs",
        ".git",
        ".git-rewrite",
        ".hg",
        ".ipynb_checkpoints",
        ".mypy_cache",
        ".nox",
        ".pants.d",
        ".pyenv",
        ".pytest_cache",
        ".pytype",
        ".ruff_cache",
        ".svn",
        ".tox",
        ".venv",
        ".vscode",
        "__pypackages__",
        "_build",
        "buck-out",
        "build",
        "dist",
        "node_modules",
        "site-packages",
        "venv",
    ]

    # Same as Black.
    line-length = 88
    indent-width = 4

    # Assume Python 3.13
    target-version = "py313"

    [lint]
    # Enable Pyflakes (`F`) and a subset of the pycodestyle (`E`)  codes by default.
    select = ["ALL"]
    ignore = [
        "COM812",
        "COM819",
        "D100",
        "D203",
        "D213",
        "D300",
        "E111",
        "E114",
        "E117",
        "ISC001",
        "ISC002",
        "Q000",
        "Q001",
        "Q002",
        "Q003",
        "W191",
    ]

    # Allow fix for all enabled rules (when `--fix`) is provided.
    fixable = ["ALL"]
    unfixable = []

    # Allow unused variables when underscore-prefixed.
    dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"

    [format]
    # Like Black, use double quotes for strings.
    quote-style = "double"

    # Like Black, indent with spaces, rather than tabs.
    indent-style = "space"

    # Like Black, respect magic trailing commas.
    skip-magic-trailing-comma = false

    # Like Black, automatically detect the appropriate line ending.
    line-ending = "auto"
    ```

=== "pyproject.toml"

    ```{.toml hl_lines=43-58}
    [tool.ruff]
    # Exclude a variety of commonly ignored directories.
    exclude = [
        ".bzr",
        ".direnv",
        ".eggs",
        ".git",
        ".git-rewrite",
        ".hg",
        ".ipynb_checkpoints",
        ".mypy_cache",
        ".nox",
        ".pants.d",
        ".pyenv",
        ".pytest_cache",
        ".pytype",
        ".ruff_cache",
        ".svn",
        ".tox",
        ".venv",
        ".vscode",
        "__pypackages__",
        "_build",
        "buck-out",
        "build",
        "dist",
        "node_modules",
        "site-packages",
        "venv",
    ]

    # Same as Black.
    line-length = 88
    indent-width = 4

    # Assume Python 3.12
    target-version = "py312"

    [tool.ruff.lint]
    # Enable Pyflakes (`F`) and a subset of the pycodestyle (`E`)  codes by default.
    select = ["ALL"]
    ignore = [
        "COM812",
        "COM819",
        "D100",
        "D203",
        "D213",
        "D300",
        "E111",
        "E114",
        "E117",
        "ISC001",
        "ISC002",
        "Q000",
        "Q001",
        "Q002",
        "Q003",
        "W191",
    ]

    # Allow fix for all enabled rules (when `--fix`) is provided.
    fixable = ["ALL"]
    unfixable = []

    # Allow unused variables when underscore-prefixed.
    dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"

    [tool.ruff.format]
    # Like Black, use double quotes for strings.
    quote-style = "double"

    # Like Black, indent with spaces, rather than tabs.
    indent-style = "space"

    # Like Black, respect magic trailing commas.
    skip-magic-trailing-comma = false

    # Like Black, automatically detect the appropriate line ending.
    line-ending = "auto"
    ```

## extensions.json
The following settings are required for automatic formatting on VSCode.
```{.json title=".vscode/extensions.json" }
{
    "python.defaultInterpreterPath": "/home/vscode/.venv/bin/python",
    "[python]": {
        "editor.codeActionsOnSave": {
            "source.fixAll": "explicit",
            "source.organizeImports": "explicit"
        },
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.formatOnSave": true,
        "editor.tabSize": 4
    }
}
```
