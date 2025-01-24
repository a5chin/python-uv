## Environment Variables
- `.env`
    - Use this file when you want to set environment variables for the project.
- `.env.local`
    - Use this file when you want to set environment variables for the local environment.

Addendum environment variables to `tools/config/settings.py`:
```{.py title="tools/config/settings.py" hl_lines="9"}
class Settings(BaseSettings):
    """Environment variables settings.

    Examples:
        >>> from tools.config import Settings
        >>> from tools.logger import Logger, LogType
        >>>
        >>> settings = Settings()
        >>> logger = Logger(
        >>>     name=__name__,
        >>>     log_type=LogType.LOCAL if settings.IS_LOCAL else LogType.GOOGLE_CLOUD
        >>> )

    """

    model_config = SettingsConfigDict(
        env_file=(".env", ".env.local"),
        env_file_encoding="utf-8",
    )

    DEBUG: bool = False
    IS_LOCAL: bool = False
```

## FastAPI
```python
from fastapi import FastAPI

from tools.config import Settings


settings = Settings()
app = FastAPI(**settings.fastapi_kwargs)
```
