import logging


class LocalFormatter(logging.Formatter):
    """Formatter for local logger."""

    def __init__(self) -> None:
        """Initialize local logger formatter."""
        from tools.logger.color import LogColor
        from tools.logger.style import LogStyle

        super().__init__()
        base = (
            f"{LogColor.GREEN}%(asctime)s{LogStyle.RESET}"
            " | "
            f"{{color}}%(levelname)-8s{LogStyle.RESET}"
            " | "
            f"{LogColor.CYAN}%(name)s{LogStyle.RESET}"
            ":"
            f"{LogColor.CYAN}%(funcName)s{LogStyle.RESET}"
            ":"
            f"{LogColor.CYAN}%(lineno)s{LogStyle.RESET}"
            " - "
            f"{{color}}%(message)s{LogStyle.RESET}"
        )
        self.formats = {
            logging.DEBUG: base.format(color=LogColor.BLUE + LogStyle.BOLD),
            logging.INFO: base.format(color=LogColor.NORMAL + LogStyle.BOLD),
            logging.WARNING: base.format(color=LogColor.YELLOW + LogStyle.BOLD),
            logging.ERROR: base.format(color=LogColor.RED + LogStyle.BOLD),
            logging.CRITICAL: base.format(color=LogColor.BLOOD + LogStyle.BOLD),
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
