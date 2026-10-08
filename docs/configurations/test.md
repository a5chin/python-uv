# Test Configurations

## `pytest.ini`
```{.ini title="pytest.ini"}
--8<-- "pytest.ini"
```

## Options Details

### `addopts` option
- `--cov=.`
    - Measure coverage for the current directory.
- `--cov-branch`
    - Measure branch coverage.
- `--cov-fail-under=75`
    - Fail if the coverage is less than 75%.
- `--cov-report=html`
    - Generate an HTML report.
- `--cov-report=term-missing`
    - Show missing lines in the terminal.
- `--import-mode=importlib`
    - Use importlib to import modules. It is recommended

### `norecursedirs` option
Ignore directories or files that match the following patterns:

- `.*`
- `__pycache__`
- `htmlcov`

### `pythonpath` option
Path specified here will be added to `sys.path` before running the tests.

### `python_files` option
Only files that match the pattern `test__*.py` will be considered as test files.
It is recommended  to reduce the number of files that pytest has to scan.

### `testpaths` option
Only the `tests` directory will be considered for running the tests.
It is recommended to reduce the number of directories that pytest has to scan.

## `settings.json`
VS Code discovers tests in `tests/` with pytest through the `python.testing.*` keys in `.vscode/settings.json` (see [VS Code Settings](ruff.md#vs-code-settings) for the full file).
