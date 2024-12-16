import logging

from tools.logger.color import Color
from tools.logger.style import Style


class LocalFormatter(logging.Formatter):
    """Formatter for local logger."""

    def __init__(self) -> None:
        """Initialize local logger formatter."""
        super().__init__()
        base = (
            f"{Color.GREEN}%(asctime)s{Style.RESET}"
            " | "
            f"{{color}}%(levelname)-8s{Style.RESET}"
            " | "
            f"{Color.CYAN}%(name)s{Style.RESET}"
            ":"
            f"{Color.CYAN}%(funcName)s{Style.RESET}"
            ":"
            f"{Color.CYAN}%(lineno)s{Style.RESET}"
            " - "
            f"{{color}}%(message)s{Style.RESET}"
        )
        self.formats = {
            logging.DEBUG: base.format(color=Color.BLUE + Style.BOLD),
            logging.INFO: base.format(color=Color.NORMAL + Style.BOLD),
            logging.WARNING: base.format(color=Color.YELLOW + Style.BOLD),
            logging.ERROR: base.format(color=Color.RED + Style.BOLD),
            logging.CRITICAL: base.format(color=Color.BLOOD + Style.BOLD),
        }

    def format(self, record: logging.LogRecord) -> str:
        """Style for local logger.

        Args:
            record (logging.LogRecord): Raw log

        Returns:
            str: Log format for local

        """
        fmt = self.formats.get(record.levelno)
        formatter = logging.Formatter(fmt)

        return formatter.format(record)
