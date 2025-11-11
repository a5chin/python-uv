# Built-in Utilities

The `tools/` package provides production-ready utility modules that you can use in your projects. These modules handle common tasks like logging, configuration management, and performance monitoring.

## Overview

The built-in utilities are designed to:

- **Reduce boilerplate** - Common patterns already implemented
- **Follow best practices** - Production-tested patterns
- **Support multiple environments** - Local development and cloud deployment
- **Type-safe** - Full type hints for better IDE support

## Available Modules

### [Logger](logger.md) - Flexible Logging System

A custom logger that supports both local development and cloud environments.

**Key features:**

- Colored console output for local development
- Structured JSON logging for Google Cloud
- Easy to switch between modes
- Built on Python's standard logging module

**Quick example:**

```python
from tools.logger import Logger, LogType

logger = Logger(__name__, log_type=LogType.LOCAL)
logger.info("Application started")
logger.error("Something went wrong")
```

[→ Full Logger documentation](logger.md)

### [Configuration](config.md) - Environment Management

Pydantic-based configuration that loads settings from environment variables and `.env` files.

**Key features:**

- Type-safe configuration
- Automatic `.env` file loading
- FastAPI integration
- Environment detection (local vs production)

**Quick example:**

```python
from tools.config import Settings

settings = Settings()  # Loads from .env and .env.local
debug_mode = settings.debug
api_url = settings.api_prefix_v1
```

[→ Full Configuration documentation](config.md)

### [Tracer](tracer.md) - Performance Monitoring

Timer decorator and context manager for measuring code execution time.

**Key features:**

- Works as decorator or context manager
- Automatic logging of execution time
- Millisecond precision
- No manual time tracking needed

**Quick example:**

```python
from tools.tracer import Timer

# As context manager
with Timer("database_query"):
    result = db.query()

# As decorator
@Timer("process_data")
def process_data(data):
    return transform(data)
```

[→ Full Tracer documentation](tracer.md)

## Module Architecture

### Package Structure

```
tools/
├── __init__.py          # Exports Logger
├── config/
│   ├── __init__.py      # Exports Settings, FastAPIKwArgs
│   ├── settings.py      # Settings class
│   └── fastapi.py       # FastAPI configuration model
├── logger/
│   ├── __init__.py      # Exports Logger, LogType, formatters
│   ├── logger.py        # Main Logger class
│   ├── type.py          # LogType enum
│   ├── local.py         # LocalFormatter
│   ├── googlecloud.py   # GoogleCloudFormatter
│   ├── color.py         # Color constants
│   └── style.py         # Log styling
└── tracer/
    ├── __init__.py      # Exports Timer
    └── timer.py         # Timer class
```

### Import Patterns

The package is designed for convenient imports:

```python
# Top-level convenience import
from tools import Logger

# Import from specific modules
from tools.logger import Logger, LogType
from tools.config import Settings, FastAPIKwArgs
from tools.tracer import Timer
```

## Common Use Cases

### FastAPI Application

```python
from fastapi import FastAPI
from tools.config import Settings
from tools.logger import Logger, LogType

settings = Settings()
logger = Logger(
    __name__,
    log_type=LogType.LOCAL if settings.IS_LOCAL else LogType.GOOGLE_CLOUD
)

app = FastAPI(**settings.fastapi_kwargs)

@app.get("/")
async def root():
    logger.info("Root endpoint called")
    return {"message": "Hello World"}
```

### Data Processing Pipeline

```python
from tools.logger import Logger
from tools.tracer import Timer

logger = Logger(__name__)

@Timer("process_dataset")
def process_dataset(data):
    logger.info(f"Processing {len(data)} records")

    with Timer("data_validation"):
        validated = validate(data)

    with Timer("data_transformation"):
        transformed = transform(validated)

    logger.info("Processing complete")
    return transformed
```

### Microservice with Configuration

```python
from tools.config import Settings
from tools.logger import Logger, LogType

class Application:
    def __init__(self):
        self.settings = Settings()
        self.logger = Logger(
            __name__,
            log_type=LogType.LOCAL if self.settings.IS_LOCAL else LogType.GOOGLE_CLOUD
        )

    def run(self):
        self.logger.info(f"Starting application in {'local' if self.settings.IS_LOCAL else 'production'} mode")
        # Application logic here
```

## Customization

All modules are designed to be extended. You can:

- Subclass `Settings` to add your own configuration fields
- Create custom formatters for the Logger
- Build on the Timer to add custom metrics

See the individual module documentation for examples.

## Testing

All utilities include comprehensive tests. See `tests/tools/` for examples:

- `test__logger.py` - Logger tests
- `test__config.py` - Configuration tests
- `test__tracer.py` - Timer tests

Run tests with:

```bash
uv run pytest tests/tools/
```

## Next Steps

- Explore each module in detail:
  - [Logger documentation](logger.md)
  - [Configuration documentation](config.md)
  - [Tracer documentation](tracer.md)
- See real-world examples in [Use Cases](../../usecases/index.md)
- Check the source code in `tools/` for implementation details
