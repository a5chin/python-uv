import logging
import sys

from google.auth.credentials import Credentials

from tools.logger.type import LogType


class Logger(logging.Logger):
    """Logger.

    Examples:
        >>> from tools.logger import Logger
        >>>
        >>>
        >>> logger = Logger(__name__)
        >>> logger.info("Logger")

    """

    def __init__(
        self,
        name: str,
        project: str | None = None,
        credentials: Credentials | None = None,
        log_type: LogType = LogType.LOCAL,
    ) -> None:
        """Initialize local logger formatter.

        Args:
            name (str): Logger name
            project (str | None, optional): Google Cloud Project ID. Defaults to None.
            credentials (Credentials | None, optional): Credentials for Google Cloud.
                                                        Defaults to None.
            log_type (LogType, optional): Local or something.
                                          Defaults to LogType.LOCAL.

        """
        super().__init__(name=name)

        if log_type == LogType.GOOGLE_CLOUD:
            import google.cloud.logging
            from google.cloud.logging_v2.handlers import StructuredLogHandler

            from tools.logger import GoogleCloudFormatter

            client = google.cloud.logging.Client(
                project=project, credentials=credentials
            )
            client.setup_logging()

            formatter = GoogleCloudFormatter()
            handler = StructuredLogHandler(stream=sys.stdout)

            handler.setFormatter(formatter)
            self.addHandler(handler)
            return

        from tools.logger import LocalFormatter

        formatter = LocalFormatter()
        handler = logging.StreamHandler(stream=sys.stdout)

        handler.setFormatter(formatter)
        self.addHandler(handler)
