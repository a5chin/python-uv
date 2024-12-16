from enum import StrEnum, auto


class LogType(StrEnum):
    """Logger type."""

    LOCAL = auto()
    GOOGLE_CLOUD = auto()
    AWS = auto()
