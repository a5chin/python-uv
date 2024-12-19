import logging


class GoogleCloudFormatter(logging.Formatter):
    """Formatter for Google Cloud logger."""

    def format(self, record: logging.LogRecord) -> str:
        """Style for Google Cloud logger.

        Args:
            record (logging.LogRecord): Raw log

        Returns:
            str: Log format for Google Cloud

        """
        from pydantic import BaseModel, PositiveInt

        class Record(BaseModel):
            """Record for Google Cloud."""

            name: str
            line: PositiveInt
            func: str
            message: str

        return Record(
            name=record.name,
            line=record.lineno,
            func=record.funcName,
            message=record.getMessage(),
        ).model_dump_json()
