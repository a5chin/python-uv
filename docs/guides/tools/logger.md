# Logger - Flexible Logging System

The Logger module provides a flexible logging system that works seamlessly in both local development and cloud environments.

## Overview

The Logger extends Python's standard `logging.Logger` with support for:

- **Local development** - Colored, formatted console output
- **Google Cloud** - Structured JSON logging compatible with Google Cloud Logging
- **Easy switching** - Change modes with a single parameter
- **Standard interface** - Uses familiar logging methods (`.info()`, `.error()`, etc.)

## Basic Usage

### Local Development

For local development, use `LogType.LOCAL` to get colored, human-readable output:

```python
from tools.logger import Logger, LogType

logger = Logger(__name__, log_type=LogType.LOCAL)
logger.info("Application started")
logger.debug("Debug information")
logger.warning("This is a warning")
logger.error("An error occurred")
```

**Output:**

```
2038-01-19 03:14:07,000 | INFO     | __main__:main:7 - Application started
2038-01-19 03:14:07,000 | DEBUG    | __main__:main:8 - Debug information
2038-01-19 03:14:07,000 | WARNING  | __main__:main:9 - This is a warning
2038-01-19 03:14:07,000 | ERROR    | __main__:main:10 - An error occurred
```

### Google Cloud Logging

For production deployment on Google Cloud, use `LogType.GOOGLE_CLOUD`:

```python
from tools.logger import Logger, LogType

logger = Logger(
    __name__,
    log_type=LogType.GOOGLE_CLOUD,
    project="my-gcp-project",
    credentials=credentials  # Optional: pass credentials object
)

logger.info("Application started in production")
```

This outputs structured JSON logs that integrate with Google Cloud Logging.

## Environment-Based Configuration

Use the Settings module to automatically select the appropriate log type:

```python
from tools.config import Settings
from tools.logger import Logger, LogType

settings = Settings()
logger = Logger(
    __name__,
    log_type=LogType.LOCAL if settings.IS_LOCAL else LogType.GOOGLE_CLOUD
)

logger.info("Logger configured based on environment")
```

Set `IS_LOCAL=true` in your `.env.local` file for local development.

## Advanced Usage

### Custom Logger Name

Use `__name__` for automatic module naming, or provide a custom name:

```python
# Automatic naming from module
logger = Logger(__name__)

# Custom name
logger = Logger("my-app")
logger.info("Custom logger name")
```

### Log Levels

All standard Python logging levels are supported:

```python
logger.debug("Detailed diagnostic information")
logger.info("General informational messages")
logger.warning("Warning messages")
logger.error("Error messages")
logger.critical("Critical error messages")
```

### Logging with Variables

Use f-strings or format strings for dynamic content:

```python
user_id = 12345
action = "login"

logger.info(f"User {user_id} performed {action}")
# Output: User 12345 performed login

logger.info("Processing %d records", record_count)
# Output: Processing 1000 records
```

### Logging Exceptions

Log exceptions with stack traces:

```python
try:
    result = risky_operation()
except Exception as e:
    logger.exception("Operation failed")
    # Logs the error message with full stack trace
```

## Complete Example

Here's a complete example showing Logger in a FastAPI application:

```python
from fastapi import FastAPI, HTTPException
from tools.config import Settings
from tools.logger import Logger, LogType

# Initialize settings and logger
settings = Settings()
logger = Logger(
    __name__,
    log_type=LogType.LOCAL if settings.IS_LOCAL else LogType.GOOGLE_CLOUD,
    project=settings.gcp_project if not settings.IS_LOCAL else None
)

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    logger.info("Application starting up")
    logger.debug(f"Debug mode: {settings.debug}")

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    logger.info(f"Fetching user {user_id}")

    try:
        user = database.get_user(user_id)
        logger.debug(f"Found user: {user.email}")
        return user
    except UserNotFound:
        logger.warning(f"User {user_id} not found")
        raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        logger.exception(f"Error fetching user {user_id}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutting down")
```

## Log Formatters

### LocalFormatter

The `LocalFormatter` provides colored, human-readable output for local development:

- Timestamps in readable format
- Color-coded log levels
- Module and line number information
- Clean formatting for console output

### GoogleCloudFormatter

The `GoogleCloudFormatter` produces structured JSON logs compatible with Google Cloud Logging:

- Structured JSON format
- Severity levels mapped to Google Cloud standards
- Automatic metadata inclusion
- Stack trace formatting for errors

## Best Practices

### 1. Use Module Names

Always use `__name__` for automatic module identification:

```python
logger = Logger(__name__)  # Good
logger = Logger("app")     # Less informative
```

### 2. Appropriate Log Levels

Choose the right level for your messages:

- `DEBUG` - Detailed diagnostic information useful during development
- `INFO` - General informational messages about application flow
- `WARNING` - Something unexpected but the application continues
- `ERROR` - Error occurred but application can recover
- `CRITICAL` - Serious error, application might not continue

### 3. Structured Logging

Include context in your log messages:

```python
# Good - includes context
logger.info(f"User {user_id} updated profile: {changes}")

# Less useful
logger.info("Profile updated")
```

### 4. Don't Log Sensitive Data

Never log passwords, tokens, or other sensitive information:

```python
# BAD - Don't do this!
logger.info(f"User logged in with password: {password}")

# Good
logger.info(f"User {user_id} logged in successfully")
```

### 5. Use Exception Logging

Use `logger.exception()` in exception handlers:

```python
try:
    process_data()
except Exception:
    logger.exception("Data processing failed")  # Includes stack trace
```

## Configuration

The Logger module uses the following configuration:

- **LogType.LOCAL**: Colored console output via `LocalFormatter`
- **LogType.GOOGLE_CLOUD**: Structured JSON via `GoogleCloudFormatter`

### Customizing Formatters

You can create custom formatters by extending the base formatters:

```python
from tools.logger.local import LocalFormatter
import logging

class CustomFormatter(LocalFormatter):
    def format(self, record: logging.LogRecord) -> str:
        # Add custom formatting logic
        formatted = super().format(record)
        return f"[CUSTOM] {formatted}"
```

## Testing

Test your logging by checking log output:

```python
import logging
from tools.logger import Logger

def test_logger():
    logger = Logger("test")

    # Capture log output
    with self.assertLogs(logger, level=logging.INFO) as cm:
        logger.info("Test message")

    assert "Test message" in cm.output[0]
```

## Related Documentation

- [Configuration Guide](config.md) - Use Settings to manage log types
- [Tracer Guide](tracer.md) - Combine with Timer for performance logging
- [FastAPI Use Case](../../usecases/fastapi.md) - Logger in web applications
