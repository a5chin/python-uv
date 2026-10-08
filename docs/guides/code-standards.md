# Code Standards

Ruff and ty enforce most of these rules automatically; run the checks in [Task Automation with nox](index.md#task-automation-with-nox) before opening a pull request.

## General Guidelines

- **Line length**: Maximum 88 characters (see [Ruff Configurations](../configurations/ruff.md))
- **Python version**: The project supports Python 3.11+ (`requires-python`); Ruff targets Python 3.14
- **Import order**: Automatically handled by Ruff
- **Naming conventions**:
    - Classes: `PascalCase`
    - Functions/variables: `snake_case`
    - Constants: `UPPER_SNAKE_CASE`
    - Private members: `_leading_underscore`

## Type Hints

All functions and methods must have type hints:

```python
# Good
def process_data(items: list[str], max_count: int = 10) -> dict[str, int]:
    """Process items and return statistics."""
    ...

# Avoid
def process_data(items, max_count=10):
    ...
```

## Docstring

All public functions, classes, and modules must have docstring:

```python
def calculate_total(items: list[float], tax_rate: float) -> float:
    """Calculate the total price including tax.

    Args:
        items: List of item prices.
        tax_rate: Tax rate as a decimal (e.g., 0.1 for 10%).

    Returns:
        Total price including tax.

    Raises:
        ValueError: If tax_rate is negative.
    """
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative")
    subtotal = sum(items)
    return subtotal * (1 + tax_rate)
```

## Code Organization

- **One class per file** (unless closely related)
- **Group related functions** in modules
- **Keep functions focused** - Single Responsibility Principle
- **Avoid deep nesting** - Maximum 3-4 levels
- **Extract complex logic** into named functions

## Testing

### Coverage

- **Minimum coverage**: 75% (including branch coverage), enforced by `pytest.ini` (see [Test Configurations](../configurations/test.md))
- **Target coverage**: 100% for new code

### Writing Tests

1. **Location**: Put tests for `tools/<module>/` in `tests/tools/test__<module>.py` (e.g. `tools/logger/` → `tests/tools/test__logger.py`)
2. **Naming**: Use the `test__*.py` pattern (double underscore); other files are not collected
3. **Structure**: One test file per module

```python
# tests/tools/test__logger.py
from tools.logger import Logger, LogType


class TestLocalLogger:
    """Test class for local logger."""

    def setup_method(self) -> None:
        """Set up logger."""
        self.logger = Logger(name=__name__, log_type=LogType.LOCAL)

    def test_name(self) -> None:
        """Test correct name of logger."""
        assert self.logger.name == __name__
```

### Running Tests

```bash
# Run all tests with coverage
uv run nox -s test

# Run a specific test file / test
uv run pytest tests/tools/test__logger.py
uv run pytest tests/tools/test__logger.py::TestLocalLogger::test_name

# View the coverage report
open htmlcov/index.html
```

### Best Practices

- **Test one thing** per test function
- **Use descriptive names** - `test_logger_handles_none_values`
- **Arrange-Act-Assert** pattern
- **Cover edge cases** - empty inputs, None, boundary values
- **Test error conditions** - expected exceptions
- **Minimize mocking** - Use real objects when possible
- **Independent tests** - No dependencies between tests

## Documentation

Update the documentation when you add features or utilities, change public APIs or configuration, add environment variables, or change the development workflow.

- **Each topic has exactly one source of truth under `docs/`.** Edit that page; `README.md`, `CONTRIBUTING.md`, and `CLAUDE.md` only link to it and must not copy its content.
- Configuration pages include the real config files with `--8<-- "<path>"` ([snippets](https://facelessuser.github.io/pymdown-extensions/extensions/snippets/)); do not paste config contents into a page.
- When adding a utility to `tools/`, add a page to `docs/guides/tools/` and list it under Available Modules and Package Structure in [`docs/guides/tools/index.md`](tools/index.md).
- When adding a page, register it in the `nav` of `mkdocs.yml` and check it with `uv run mkdocs build --strict`.
- Provide code examples and test them before committing.

## Common Issues

### Test Coverage Below 75%

Run `uv run nox -s test`, open `htmlcov/index.html` to find uncovered lines, and add tests for them.

### Lint Errors

```bash
uv run ruff check . --fix   # Auto-fix Ruff issues
uv run ruff format .        # Format code
uv run ty check             # Check type errors
```

If type errors persist, add type hints or use `# type: ignore` with a justification.

### Pre-commit Hook Failures

Run `uv run pre-commit run --all-files` to see what failed. Formatting and trailing whitespace are fixed by the hooks; fix JSON / YAML / TOML syntax errors manually, then `git add` and commit again.

### Merge Conflicts

```bash
git checkout main
git pull origin main
git checkout your-branch
git merge main
# Resolve conflicts, then:
git add .
git commit -m "fix: Resolve merge conflicts with main"
git push origin your-branch
```

### `uv.lock` Out of Sync

If CI fails with dependency resolution errors, run `uv lock` and commit the updated `uv.lock`.

### Import Errors in Tests

If tests fail with `ModuleNotFoundError`, run `uv sync` and import from the package root (e.g. `from tools.logger import Logger`, not `from logger import Logger`).
