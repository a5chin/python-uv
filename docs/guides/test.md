# Test User Guides on this repository

!!! TIP
    Official documentation for pytest is available at [https://docs.pytest.org/en/stable](https://docs.pytest.org/en/stable)

## Run pytest command
```sh
uv run pytest
```

```sh
================================================ test session starts ================================================
platform linux -- Python 3.14.0, pytest-9.0.1, pluggy-1.6.0
rootdir: /workspace
configfile: pytest.ini
testpaths: tests
plugins: anyio-4.11.0, cov-7.0.0
collected 8 items

tests/tools/test__config.py ..                                                                                             [ 25%]
tests/tools/test__logger.py ....                                                                                           [ 75%]
tests/tools/test__tracer.py ..                                                                                             [100%]

================================================ tests coverage ================================================
________________________________________ coverage: platform linux, python 3.14.0-final-0 _________________________________________

Name                          Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------------------------------
tools/config/fastapi.py           2      0      0      0   100%
tools/config/settings.py         20      0      0      0   100%
tools/logger/color.py            12      0      0      0   100%
tools/logger/googlecloud.py       6      0      0      0   100%
tools/logger/local.py            12      0      0      0   100%
tools/logger/logger.py           23      0      2      0   100%
tools/logger/style.py             7      0      0      0   100%
tools/logger/type.py              5      0      0      0   100%
tools/tracer/timer.py            16      0      0      0   100%
-------------------------------------------------------------------------
TOTAL                           103      0      2      0   100%
Coverage HTML written to dir htmlcov
Required test coverage of 75% reached. Total coverage: 100.00%
================================================ 8 passed in 1.23s ================================================
```

## Run pytest on VS Code


![](../img/test_with_coverage.png){ loading=lazy }
/// caption
Test with coverage on VS Code
///

![](../img/coverage_on_editor.png){ loading=lazy }
/// caption
Code coverage on editor
///

## Configuration for Test
If you want to configure the Test hook, visit the [Configuration for Test](../configurations/test.md) page.
