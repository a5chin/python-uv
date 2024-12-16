from enum import StrEnum


class LogStyle(StrEnum):
    """Style code logger."""

    BOLD = "\033[1m"
    ULINE = "\033[4m"
    BLINK = "\033[5m"
    INVERT = "\033[7m"
    RESET = "\x1b[0m"
