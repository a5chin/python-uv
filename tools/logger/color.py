from enum import StrEnum


class LogColor(StrEnum):
    """Color code for logger."""

    NORMAL = "\033[0m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    GREY = "\033[37m"
    BLOOD = "\033[41m"
