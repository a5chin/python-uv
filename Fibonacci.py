def Fib(n) -> int:  # noqa: N802, D103, ANN001
    if n == 1:
        return 0
    elif n == 2:  # noqa: RET505, PLR2004
        return 1
    else:
        return Fib(n - 1) + Fib(n - 2)
