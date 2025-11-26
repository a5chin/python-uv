import time
from contextlib import ContextDecorator


class Timer(ContextDecorator):
    """Timer ContextManager and Decorator.

    Examples:
        >>> import time
        >>>
        >>> from tools.tracer import Timer
        >>>
        >>> with Timer("examples"):
        >>>     time.sleep(1)

        >>> import time
        >>>
        >>> from tools.tracer import Timer
        >>>
        >>>
        >>> @Timer("sleep")
        >>> def sleep(t: int = 1) -> None:
        >>>     time.sleep(t)
        >>>
        >>>
        >>> sleep(1)

    """

    def __init__(self, name: str) -> None:
        """Initialize Timer.

        Args:
            name (str): Log name

        """
        super().__init__()
        self.name = name

    def __enter__(self) -> None:
        """Run when enter ContextManager or Decorator."""
        self.start = time.time()

    def __exit__(self, *exc: object) -> None:
        """Run when exit ContextManager or Decorator."""
        self.end = time.time()

        from tools import Logger

        logger = Logger(self.name)
        logger.debug("executed in %f ms", self._duration * 1_000)

    @property
    def _duration(self) -> float:
        """Return duration in seconds."""
        return self.end - self.start
