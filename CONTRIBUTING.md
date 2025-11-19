# Contributing to python-uv

Thank you for your interest in contributing to python-uv! This document provides guidelines and instructions for contributing to this project.

## Table of Contents

- [Quick Start for Contributors](#quick-start-for-contributors)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Pull Request Process](#pull-request-process)
- [Code Standards](#code-standards)
- [Testing Requirements](#testing-requirements)
- [Documentation Guidelines](#documentation-guidelines)
- [Common Issues](#common-issues)
- [Getting Help](#getting-help)

## Quick Start for Contributors

1. **Fork and clone** the repository
2. **Set up** your development environment
3. **Create a branch** for your changes
4. **Make changes** following our code standards
5. **Run tests** and quality checks
6. **Submit a pull request** using our template

## Development Setup

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) package manager
- Git
- (Optional) Docker and VSCode with Dev Containers extension

### Setup Steps

#### Option 1: Using Dev Container (Recommended)

```bash
# Clone the repository
git clone https://github.com/a5chin/python-uv.git
cd python-uv

# Open in VSCode
code .

# When prompted, click "Reopen in Container"
```

#### Option 2: Local Setup

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone https://github.com/a5chin/python-uv.git
cd python-uv

# Install dependencies
uv sync

# Install pre-commit hooks
uv run pre-commit install
```

### Verify Your Setup

```bash
# Run tests
uv run nox -s test

# Run linters
uv run nox -s lint -- --pyright --ruff

# Format code
uv run nox -s fmt
```

If all commands complete successfully, you're ready to contribute!

## Making Changes

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

Branch naming conventions:
- `feature/` - New features
- `fix/` - Bug fixes
- `hotfix/` - Hotfix
- `release/` - Release changes

### 2. Make Your Changes

Follow these guidelines while making changes:

- **Write clear, focused commits** - Each commit should represent a single logical change
- **Follow code standards** - See [Code Standards](#code-standards) section
- **Add tests** - All new code should have corresponding tests
- **Update documentation** - Keep docs in sync with code changes

### 3. Commit Your Changes

Use descriptive commit messages:

```bash
# Good commit messages
git commit -m "add: CloudWatch logging support"
git commit -m "fix: Handle None values in Logger.format()"
git commit -m "update: Improve type hints in Settings class"
git commit -m "refactor: Simplify Timer context manager logic"
git commit -m "test: Add edge cases for config loading"
git commit -m "docs: Update contributing guidelines"

# Avoid
git commit -m "updates"
git commit -m "fix bug"
git commit -m "changes"
```

## Pull Request Process

### Before Submitting

**You MUST run all quality checks before submitting your PR:**

```bash
# 1. Format code
uv run nox -s fmt

# 2. Run linters
uv run nox -s lint -- --pyright --ruff

# 3. Run tests with coverage
uv run nox -s test

# 4. Run pre-commit hooks
uv run pre-commit run --all-files
```

All checks must pass. PRs with failing checks will not be reviewed.

### Submitting Your PR

1. **Push your branch** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request** on GitHub
   - The PR template will be auto-populated
   - Fill out all sections completely
   - Link related issues using `Fixes #123` or `Relates to #456`

3. **PR Template Sections to Complete:**

   - **Summary** - What and why you made these changes
   - **Type of Change** - Select applicable change types
   - **Related Issues** - Link to issues
   - **Changes Made** - List main changes
   - **Testing** - Confirm all test commands passed
   - **Pre-Submission Checklist** - Verify all items
   - **Breaking Changes** - Document if applicable
   - **Additional Notes** - Screenshots, performance notes, etc.

### PR Review Process

1. **Automated checks** run on your PR (CI/CD workflows)
2. **Maintainers review** your code using the review checklist
3. **Address feedback** if changes are requested
4. **PR is merged** once approved

**Review Timeline:**
- Initial review: Within 2-3 business days
- Follow-up reviews: Within 1-2 business days

## Code Standards

### General Guidelines

- **Line length**: Maximum 88 characters (Black-compatible)
- **Python version**: Target Python 3.14
- **Import order**: Automatically handled by Ruff
- **Naming conventions**:
  - Classes: `PascalCase`
  - Functions/variables: `snake_case`
  - Constants: `UPPER_SNAKE_CASE`
  - Private members: `_leading_underscore`

### Type Hints

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

### Docstrings

All public functions, classes, and modules must have docstrings:

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

### Code Organization

- **One class per file** (unless closely related)
- **Group related functions** in modules
- **Keep functions focused** - Single Responsibility Principle
- **Avoid deep nesting** - Maximum 3-4 levels
- **Extract complex logic** into named functions

### Ruff Rules
Run `uv run ruff check .` to see all violations.

## Testing Requirements

### Coverage Requirements

- **Minimum coverage**: 75% (including branch coverage)
- **Target coverage**: 100% for new code
- **Coverage report**: Generated automatically when running tests

### Writing Tests

1. **Location**: Mirror the structure of `tools/` in `tests/`
2. **Naming**: Use `test__*.py` pattern (double underscore)
3. **Structure**: One test file per module

Example test structure:

```python
# tests/tools/test__logger.py
import logging
from tools.logger import Logger, LogType

def test_logger_local_format():
    """Test local logger formatting."""
    logger = Logger(__name__, log_type=LogType.LOCAL)
    assert logger.level == logging.INFO

def test_logger_handles_none():
    """Test logger handles None values correctly."""
    logger = Logger(__name__)
    # Test implementation
    ...
```

### Running Tests

```bash
# Run all tests with coverage
uv run nox -s test

# Run specific test file
uv run pytest tests/tools/test__logger.py

# Run specific test function
uv run pytest tests/tools/test__logger.py::test_logger_local_format

# View coverage report
open htmlcov/index.html
```

### Test Best Practices

- **Test one thing** per test function
- **Use descriptive names** - `test_logger_handles_none_values`
- **Arrange-Act-Assert** pattern
- **Cover edge cases** - empty inputs, None, boundary values
- **Test error conditions** - expected exceptions
- **Minimize mocking** - Use real objects when possible
- **Independent tests** - No dependencies between tests

## Documentation Guidelines

### When to Update Documentation

Update documentation when you:
- Add new features or utilities
- Change public APIs
- Modify configuration options
- Add environment variables
- Change development workflow
- Fix bugs that were caused by unclear documentation

### Documentation Files

- **README.md** - High-level overview, quick start, features
- **CLAUDE.md** - Development workflow for Claude Code users
- **CONTRIBUTING.md** - This file (contribution guidelines)
- **docs/** - Detailed guides and references
  - `docs/guides/` - Usage guides and tutorials
  - `docs/configurations/` - Configuration references
  - `docs/usecases/` - Real-world examples

### Documentation Standards

- Use clear, concise language
- Provide code examples for new features
- Include both "how" and "why" explanations
- Keep examples up-to-date with code changes
- Use proper markdown formatting
- Test all code examples before committing

## Common Issues

### Test Coverage Below 75%

**Problem**: Coverage is 72%, below the required 75%

**Solution**:
```bash
# Check coverage report
uv run nox -s test

# View detailed HTML report to see uncovered lines
open htmlcov/index.html

# Add tests for uncovered lines
```

### Linting Errors

**Problem**: `uv run nox -s lint` fails

**Solution**:
```bash
# Auto-fix Ruff issues
uv run ruff check . --fix

# Format code
uv run ruff format .

# Check type errors
uv run pyright

# If type errors persist, add type hints or use type: ignore with justification
```

### Pre-commit Hook Failures

**Problem**: Git commit is blocked by pre-commit hooks

**Solution**:
```bash
# See what failed
uv run pre-commit run --all-files

# Common fixes:
# - Ruff formatting: Auto-fixed by the hook
# - Trailing whitespace: Auto-fixed by the hook
# - JSON/YAML/TOML: Fix syntax errors manually

# Retry commit after fixes
git add .
git commit -m "Your message"
```

### Merge Conflicts

**Problem**: Your branch has conflicts with main

**Solution**:
```bash
# Update main branch
git checkout main
git pull origin main

# Go back to your branch
git checkout your-branch

# Merge main into your branch
git merge main

# Resolve conflicts in your editor
# After resolving, stage the files
git add .

# Complete the merge
git commit -m "Resolve merge conflicts with main"

# Push updated branch
git push origin your-branch
```

### `uv.lock` Out of Sync

**Problem**: CI fails with dependency resolution errors

**Solution**:
```bash
# Regenerate lock file
uv lock

# Commit the updated lock file
git add uv.lock
git commit -m "Update: Regenerate uv.lock"
```

### Import Errors in Tests

**Problem**: Tests fail with `ModuleNotFoundError`

**Solution**:
```bash
# Ensure dependencies are installed
uv sync

# If issue persists, check that you're using the correct import paths
# Example: Use `from tools.logger import Logger` not `from logger import Logger`
```

## Getting Help

### Resources

- **Documentation**: https://a5chin.github.io/python-uv
- **Detailed Contributing Guide**: [CONTRIBUTING.md](CONTRIBUTINGmd)
- **PR Template**: [.github/pull_request_template.md](.github/pull_request_template.md)

### Questions and Discussions

- **GitHub Issues**: For bug reports and feature requests
- **GitHub Discussions**: For questions and general discussions
- **Pull Request Comments**: For questions about specific code changes

---

## Summary Checklist

Before submitting your PR, verify:

- [ ] Code follows project standards (Ruff, Pyright, type hints, docstrings)
- [ ] All tests pass: `uv run nox -s test` (coverage ≥ 75%)
- [ ] Linting passes: `uv run nox -s lint -- --pyright --ruff`
- [ ] Code is formatted: `uv run nox -s fmt`
- [ ] Pre-commit hooks pass: `uv run pre-commit run --all-files`
- [ ] Documentation updated (README, CLAUDE.md, or docs/)
- [ ] New test files follow `test__*.py` naming convention
- [ ] Dependencies added via `uv add` (not manual edits)
- [ ] `uv.lock` is updated and committed
- [ ] PR template is completely filled out
- [ ] Breaking changes are documented (if applicable)
- [ ] Related issues are linked in PR description

**Thank you for contributing to python-uv! 🎉**
