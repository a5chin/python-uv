# ty Configurations

!!! TIP
    Official documentation for ty is available at [https://github.com/astral-sh/ty](https://github.com/astral-sh/ty)

!!! INFO
    ty is a fast type checker for Python built by Astral (the creators of uv and Ruff).

```{.toml title="ty.toml"}
[src]
include = ["tools", "tests", "noxfile.py"]
exclude = ["**/__pycache__", ".pytest_cache", ".ruff_cache", ".venv"]
```

## Configuration Options

- **include**: List of directories or files to include in type checking
  - Currently includes `tools/` package, `tests/` directory, and `noxfile.py`

- **exclude**: List of patterns to exclude from type checking
  - Cache directories: `**/__pycache__`, `.pytest_cache`, `.ruff_cache`
  - Virtual environment: `.venv`

## Adding New Directories

!!! DANGER
    If you create new directories in the root directory that should be type-checked, you must add them to the `include` list in the `ty.toml` file.

Example:
```toml
[src]
include = ["tools", "tests", "noxfile.py", "your_new_package"]
exclude = ["**/__pycache__", ".pytest_cache", ".ruff_cache", ".venv"]
```
