import logging
import sys

from tools.logger.type import Type


class Logger(logging.Logger):
    """Logger."""

    def __init__(self, name: str, log_type: Type = Type.LOCAL) -> None:
        """Initialize local logger formatter.

        Args:
            name (str): Logger name
            log_type (Type, optional): Local or something. Defaults to Type.LOCAL.

        """
        super().__init__(name=name)
        if log_type == Type.LOCAL:
            from tools.logger import LocalFormatter

            formatter = LocalFormatter()
            handler = logging.StreamHandler(stream=sys.stdout)

            handler.setFormatter(formatter)
            self.addHandler(handler)
        elif log_type == Type.GOOGLE_CLOUD:
            import google.cloud.logging
            from google.cloud.logging_v2.handlers import StructuredLogHandler

            from tools.logger import GoogleCloudFormatter

            client = google.cloud.logging.Client()
            client.setup_logging()

            formatter = GoogleCloudFormatter()
            handler = StructuredLogHandler(stream=sys.stdout)

            handler.setFormatter(formatter)
            self.addHandler(handler)
