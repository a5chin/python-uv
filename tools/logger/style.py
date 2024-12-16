from enum import StrEnum


class Style(StrEnum):
    """Style code."""

    BOLD = "\033[1m"
    ULINE = "\033[4m"
    BLINK = "\033[5m"
    INVERT = "\033[7m"
    RESET = "\x1b[0m"
