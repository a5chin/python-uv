from pydantic import BaseModel


class FastAPIKwArgs(BaseModel):
    """FastAPI kwargs."""

    debug: bool
    title: str
    version: str
    summary: str | None
    description: str
    openapi_url: str
    docs_url: str
    redoc_url: str
    openapi_prefix: str
