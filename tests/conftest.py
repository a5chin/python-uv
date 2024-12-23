import pytest

from tools import Settings


@pytest.fixture
def settings() -> Settings:
    """Fixture for settings."""
    return Settings()
