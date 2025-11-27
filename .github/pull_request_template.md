## Summary

<!-- Briefly describe what this PR does and why it's needed -->


## Type of Change

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Refactoring (code improvement without changing functionality)
- [ ] Documentation update
- [ ] Performance improvement
- [ ] CI/CD or tooling change
- [ ] Dependency update

## Related Issues

<!-- Link to related issues (e.g., Fixes #123, Relates to #456) -->

Fixes #
Relates to #

## Changes Made

<!-- List the main changes in this PR -->

-
-
-

## Testing

<!-- Describe how you tested these changes -->

**Test Commands Run:**
- [ ] `uv run nox -s test` (all tests passed, coverage ≥ 75%)
- [ ] `uv run nox -s lint -- --pyright --ruff` (no errors)
- [ ] `uv run nox -s fmt` (formatting applied)
- [ ] `uv run pre-commit run --all-files` (all hooks passed)

**Testing Notes:**
<!-- Add any relevant testing details, edge cases covered, or manual testing steps -->


## Pre-Submission Checklist

<!-- Verify ALL items before requesting review -->

### Code Quality & Tests
- [ ] All functions/methods have type hints
- [ ] Code has docstring for public APIs
- [ ] New test files follow `test__*.py` naming convention
- [ ] Tests are meaningful and cover edge cases

### Dependencies & Documentation
- [ ] Used `uv add` for dependencies (not manual `pyproject.toml` edits)
- [ ] `uv.lock` is updated and committed
- [ ] Documentation updated (`README.md`, `CLAUDE.md`, or `docs/` if applicable)
- [ ] Environment variables documented (if new ones added to `Settings`)

### Configuration Changes
- [ ] No configuration changes
- OR if config changed:
  - [ ] `.env` updated with new variables and defaults
  - [ ] `Settings` class updated
  - [ ] No secrets committed (use `.env.local` for sensitive values)

## Breaking Changes

- [ ] This PR does NOT include breaking changes

<!-- If there ARE breaking changes, describe them below -->

**Breaking Changes Details:**
<!-- Describe what breaks, migration path, and affected users/systems -->


## Additional Notes

<!-- Add screenshots, performance notes, deployment instructions, or reviewer guidance if needed -->
