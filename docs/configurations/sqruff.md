# sqruff Configurations

!!! TIP
    Official documentation for sqruff is available at [https://github.com/quarylabs/sqruff](https://github.com/quarylabs/sqruff)

```{.ini title=".sqruff"}
--8<-- ".sqruff"
```

## Configuration Options

- **`dialect`**: SQL dialect (BigQuery)
- **`templater`**: Jinja templates in SQL files are rendered before linting
- **`max_line_length`**: 80 characters
- **`rules`**: All rules are enabled; list rules to skip in `exclude_rules`
- **Indentation**: 2 spaces, and `JOIN` clauses are indented
- **`ambiguous.join`**: Join types must be written explicitly (e.g. `INNER JOIN`, not `JOIN`)

Files listed in `.sqruffignore` are skipped.

## Usage

```bash
# Lint / format SQL files via nox
uv run nox -s lint -- --sqruff
uv run nox -s fmt -- --sqruff

# Run sqruff directly
uv run sqruff lint
uv run sqruff fix
```
