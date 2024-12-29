import pytest

from tools.config import FastAPIKwArgs, Settings


class TestSettings:
    """Test class for Settings."""

    @pytest.mark.usefixtures("settings")
    def test_local(self, settings: Settings) -> None:
        """Test local settings."""
        assert settings.IS_LOCAL

    @pytest.mark.usefixtures("settings")
    def test_fastapi_kwargs(self, settings: Settings) -> None:
        """Test fastapi_kwargs."""
        assert (
            settings.fastapi_kwargs
            == FastAPIKwArgs(
                debug=False,
                title="FastAPI",
                summary=None,
                description="",
                version="0.1.0",
                openapi_url="/openapi.json",
                docs_url="/docs",
                redoc_url="/redoc",
                openapi_prefix="",
            ).model_dump()
        )
