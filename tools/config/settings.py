from typing import Any

from pydantic_settings import BaseSettings, SettingsConfigDict

from tools.config.fastapi import FastAPIKwArgs


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

    IS_LOCAL: bool = False

    debug: bool = False
    title: str = "FastAPI"
    summary: str | None = None
    description: str = ""
    version: str = "0.1.0"
    openapi_url: str = "/openapi.json"
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    openapi_prefix: str = ""
    api_prefix_v1: str = "/api/v1"
    allowed_hosts: list[str] = ["*"]

    @property
    def fastapi_kwargs(self) -> dict[str, Any]:
        """FastAPI kwargs."""
        return FastAPIKwArgs(
            debug=self.debug,
            title=self.title,
            summary=self.summary,
            description=self.description,
            version=self.version,
            openapi_url=self.openapi_url,
            docs_url=self.docs_url,
            redoc_url=self.redoc_url,
            openapi_prefix=self.openapi_prefix,
        ).model_dump()
