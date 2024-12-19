import logging
import sys

from tools.logger.type import LogType


class Logger(logging.Logger):
    """Logger."""

    def __init__(self, name: str, log_type: LogType = LogType.LOCAL) -> None:
        """Initialize local logger formatter.

        Args:
            name (str): Logger name
            log_type (LogType, optional): Local or something.
                                          Defaults to LogType.LOCAL.

        """
        super().__init__(name=name)

        if log_type == LogType.LOCAL:
            from tools.logger import LocalFormatter

            formatter = LocalFormatter()
            handler = logging.StreamHandler(stream=sys.stdout)

            handler.setFormatter(formatter)
            self.addHandler(handler)
        elif log_type == LogType.GOOGLE_CLOUD:
            import google.cloud.logging
            from google.cloud.logging_v2.handlers import StructuredLogHandler

            from tools.logger import GoogleCloudFormatter

            client = google.cloud.logging.Client()
            client.setup_logging()

            formatter = GoogleCloudFormatter()
            handler = StructuredLogHandler(stream=sys.stdout)

            handler.setFormatter(formatter)
            self.addHandler(handler)
