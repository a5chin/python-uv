from tools.tracer import Timer


class TestTimer:
    """Test class for Timer."""

    def test_contextmanager(self) -> None:
        """Test for ContextManager."""
        with Timer("ContextManager"):
            pass

    @Timer("Decorator")
    def test_decorator(self) -> None:
        """Test for Decorator."""
