import pytest

from tools.config import Settings


@pytest.fixture
def settings() -> Settings:
    """Fixture for settings."""
    return Settings()
