# Contributing to python-uv

Thank you for your interest in contributing to python-uv! This document describes how to propose changes. Development details live in the [documentation](docs/index.md), which this page links to.

All contributors must follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## Table of Contents

- [Quick Start for Contributors](#quick-start-for-contributors)
- [Making Changes](#making-changes)
- [Pull Request Process](#pull-request-process)
- [Getting Help](#getting-help)

## Quick Start for Contributors

1. **Set up** your development environment: [Getting Started](docs/getting-started/index.md)
2. **Create a branch** from `main`: [Branch Strategy & Release Flow](docs/guides/branch-strategy.md#branches)
3. **Make changes** following the [Code Standards](docs/guides/code-standards.md)
4. **Run the quality checks**: [Before Submitting](#before-submitting)
5. **Submit a pull request** to `main` using our template

## Making Changes

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

Use a prefix from [Branches](docs/guides/branch-strategy.md#branches) (`feature/`, `fix/`, `hotfix/`, `refactor/`). What happens after your PR is merged into `main` is described in [Branch Strategy & Release Flow](docs/guides/branch-strategy.md).

### 2. Make Your Changes

- **Write clear, focused commits** - Each commit should represent a single logical change
- **Follow the [Code Standards](docs/guides/code-standards.md)** - including type hints, docstrings, and tests
- **Update documentation** - Edit the page under `docs/` that owns the topic (see [Documentation](docs/guides/code-standards.md#documentation))

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

**You MUST pass all quality checks before submitting your PR.** The commands and their flags are listed in [Task Automation with nox](docs/guides/index.md#task-automation-with-nox):

- [ ] Code is formatted: `uv run nox -s fmt -- --ruff --sqruff`
- [ ] Linting passes: `uv run nox -s lint -- --ruff --sqruff --ty`
- [ ] All tests pass: `uv run nox -s test` (coverage ≥ 75%)
- [ ] Pre-commit hooks pass: `uv run pre-commit run --all-files`
- [ ] New test files follow the `test__*.py` naming convention
- [ ] Dependencies are added via `uv add`, and `uv.lock` is committed
- [ ] Documentation is updated under `docs/`
- [ ] Breaking changes are documented (if applicable)

PRs with failing checks will not be reviewed. If a check fails, see [Common Issues](docs/guides/code-standards.md#common-issues).

### Submitting Your PR

1. **Push your branch** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request** against `main` on GitHub
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

1. **Automated checks** run on your PR (see [CI/CD Workflows](docs/guides/ci-cd.md))
2. **Maintainers review** your code using the review checklist
3. **Address feedback** if changes are requested
4. **PR is merged** once approved

**Review Timeline:**
- Initial review: Within 2-3 business days
- Follow-up reviews: Within 1-2 business days

## Getting Help

### Resources

- **Documentation**: https://a5chin.github.io/python-uv (source: [`docs/`](docs/index.md))
- **PR Template**: [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md)

### Questions and Discussions

- **GitHub Issues**: For bug reports and feature requests
- **GitHub Discussions**: For questions and general discussions
- **Pull Request Comments**: For questions about specific code changes

**Thank you for contributing to python-uv! 🎉**
