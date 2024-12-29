# Pyright Configurations

!!! TIP
    Official documentation for Pyright is available at [https://microsoft.github.io/pyright](https://microsoft.github.io/pyright)

!!! DANGER
    If you want to create new directories in the root directory, you must add them to the `include` list in the `pyrightconfig.json` file.

```{.json title="pyrightconfig.json"}
{
    "pythonVersion": "3.13",
    "pythonPlatform": "All",
    "venv": ".venv",
    "typeCheckingMode": "standard",
    "include": [
        "tools"
    ],
    "exclude": [
        "**/__pycache__",
        ".pytest_cache",
        ".ruff_cache",
        ".venv"
    ],
}
```
