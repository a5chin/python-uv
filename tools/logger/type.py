from enum import StrEnum, auto


class Type(StrEnum):
    """Logger type."""

    LOCAL = auto()
    GOOGLE_CLOUD = auto()
    AWS = auto()
