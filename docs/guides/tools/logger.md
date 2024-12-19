```python
from tools import Logger


def main() -> None:
    """Sample function."""
    logger = Logger(__name__)
    logger.info("Hello, World!")


if __name__ == "__main__":
    main()
```

!!! NOTE
    ```sh
    2038-01-19 03:14:07,000 | INFO     | __main__:main:7 - Hello, World!
    ```
