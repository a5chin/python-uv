# Configuration - Environment Management

The Configuration module provides type-safe, environment-based settings management using Pydantic. It automatically loads configuration from `.env` files and environment variables.

## Overview

The Configuration module offers:

- **Type safety** - Pydantic validation ensures correct types
- **Auto-loading** - Reads `.env` and `.env.local` files automatically
- **Environment detection** - Distinguish between local and production
- **FastAPI integration** - Ready-to-use FastAPI configuration
- **Easy extension** - Add custom settings by extending the base class

## Basic Usage

### Loading Settings

```python
from tools.config import Settings

# Automatically loads from .env and .env.local
settings = Settings()

# Access configuration values
debug_mode = settings.debug
api_prefix = settings.api_prefix_v1
is_local = settings.IS_LOCAL
```

### Environment Files

The module loads configuration from two files in order:

1. `.env` - Base configuration (committed to git)
2. `.env.local` - Local overrides (not committed, in `.gitignore`)

**`.env`** (shared configuration):
```bash
DEBUG=false
TITLE=My Application
API_PREFIX_V1=/api/v1
```

**`.env.local`** (local overrides):
```bash
IS_LOCAL=true
DEBUG=true
```

## Available Settings

### Default Configuration Fields

```python
class Settings(BaseSettings):
    # Environment detection
    IS_LOCAL: bool = False

    # FastAPI settings
    debug: bool = False
    title: str = "FastAPI"
    summary: str | None = None
    description: str = ""
    version: str = "0.1.0"
    openapi_url: str = "/openapi.json"
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    openapi_prefix: str = ""

    # API configuration
    api_prefix_v1: str = "/api/v1"

    # CORS settings
    allowed_hosts: list[str] = ["*"]
```

## FastAPI Integration

### Basic FastAPI Setup

```python
from fastapi import FastAPI
from tools.config import Settings

settings = Settings()

# Use fastapi_kwargs property for clean initialization
app = FastAPI(**settings.fastapi_kwargs)

@app.get("/")
async def root():
    return {
        "title": settings.title,
        "version": settings.version,
        "environment": "local" if settings.IS_LOCAL else "production"
    }
```

### FastAPI with Custom Configuration

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tools.config import Settings

settings = Settings()
app = FastAPI(**settings.fastapi_kwargs)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_hosts,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Extending Settings

### Adding Custom Fields

Extend the `Settings` class to add your own configuration:

```python
from tools.config import Settings as BaseSettings

class Settings(BaseSettings):
    # Add your custom fields
    DATABASE_URL: str = "sqlite:///./app.db"
    SECRET_KEY: str
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

    # Add validation
    @property
    def redis_url(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"
```

Then in your `.env` file:

```bash
DATABASE_URL=postgresql://user:pass@localhost/db_name
SECRET_KEY=your-secret-key-here
REDIS_HOST=redis.example.com
REDIS_PORT=6380
```

### Database Configuration Example

```python
from pydantic import PostgresDsn
from tools.config import Settings as BaseSettings

class DatabaseSettings(BaseSettings):
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str = "app"
    POSTGRES_PORT: int = 5432

    @property
    def database_url(self) -> str:
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

# Usage
settings = DatabaseSettings()
engine = create_engine(settings.database_url)
```

## Environment-Based Behavior

### Conditional Logic

Use `IS_LOCAL` to change behavior based on environment:

```python
from tools.config import Settings
from tools.logger import Logger, LogType

settings = Settings()

# Select log type based on environment
logger = Logger(
    __name__,
    log_type=LogType.LOCAL if settings.IS_LOCAL else LogType.GOOGLE_CLOUD
)

# Configure database
if settings.IS_LOCAL:
    DATABASE_URL = "sqlite:///./dev.db"
else:
    DATABASE_URL = settings.production_database_url

# Debug mode
app = FastAPI(
    **settings.fastapi_kwargs,
    debug=settings.debug
)
```

## Complete Example

Here's a complete example of a FastAPI application with extended configuration:

```python
from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from tools.config import Settings as BaseSettings
from tools.logger import Logger, LogType

class AppSettings(BaseSettings):
    # Database
    DATABASE_URL: str = "sqlite:///./app.db"

    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # External APIs
    EXTERNAL_API_KEY: str = ""
    EXTERNAL_API_URL: str = "https://api.example.com"

# Initialize
settings = AppSettings()
logger = Logger(
    __name__,
    log_type=LogType.LOCAL if settings.IS_LOCAL else LogType.GOOGLE_CLOUD
)

# Database
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# FastAPI
app = FastAPI(**settings.fastapi_kwargs)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
async def startup():
    logger.info(f"Starting application: {settings.title}")
    logger.info(f"Environment: {'local' if settings.IS_LOCAL else 'production'}")
    logger.debug(f"Database: {settings.DATABASE_URL}")

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": settings.version,
        "environment": "local" if settings.IS_LOCAL else "production"
    }
```

## Best Practices

### 1. Never Commit Secrets

Always keep sensitive data in `.env.local`:

```bash
# .gitignore (should already include this)
.env.local
```

### 2. Provide Defaults

Set sensible defaults for non-sensitive configuration:

```python
class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./dev.db"  # Safe default
    SECRET_KEY: str  # No default - must be provided
```

### 3. Use Type Annotations

Leverage Pydantic's type validation:

```python
class Settings(BaseSettings):
    PORT: int = 8000  # Validates as integer
    DEBUG: bool = False  # Validates as boolean
    ALLOWED_HOSTS: list[str] = ["*"]  # Validates as list
```

### 4. Document Your Settings

Add docstring to custom settings:

```python
class Settings(BaseSettings):
    """Application configuration.

    Loads from .env and .env.local files.
    """

    DATABASE_URL: str = "sqlite:///./app.db"
    """Database connection string."""

    SECRET_KEY: str
    """Secret key for JWT tokens. Must be set in .env.local."""
```

### 5. Validate Related Settings

Use Pydantic validators for complex validation:

```python
from pydantic import field_validator

class Settings(BaseSettings):
    MIN_VALUE: int = 0
    MAX_VALUE: int = 100

    @field_validator('MAX_VALUE')
    @classmethod
    def validate_max_greater_than_min(cls, v, info):
        if 'MIN_VALUE' in info.data and v <= info.data['MIN_VALUE']:
            raise ValueError('MAX_VALUE must be greater than MIN_VALUE')
        return v
```

## Testing

### Testing with Override

Override settings in tests:

```python
import pytest
from tools.config import Settings

def test_with_custom_settings():
    settings = Settings(
        DEBUG=True,
        IS_LOCAL=True,
        DATABASE_URL="sqlite:///:memory:"
    )

    assert settings.DEBUG is True
    assert settings.IS_LOCAL is True
```

### Testing Environment Loading

```python
import os
from tools.config import Settings

def test_env_loading(monkeypatch):
    monkeypatch.setenv("DEBUG", "true")
    monkeypatch.setenv("TITLE", "Test App")

    settings = Settings()

    assert settings.debug is True
    assert settings.title == "Test App"
```

## Related Documentation

- [Logger Guide](logger.md) - Use Settings to configure logging
- [FastAPI Use Case](../../usecases/fastapi.md) - Full FastAPI integration example
- [Pydantic Settings Documentation](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
