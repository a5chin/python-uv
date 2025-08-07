## Timer

### Decorator
```{.py hl_lines="6"}
import time

from tools.tracer import Timer


@Timer("sleep")
def sleep(t: int = 1) -> None:
    time.sleep(t)


sleep(1)
```

!!! NOTE
    ```sh
    2038-01-19 03:14:07,000 | DEBUG    | sleep:__exit__:50 - executed in 1000.000000 ms
    ```

### ContextManager
```{.py hl_lines="5"}
import time

from tools.tracer import Timer

with Timer("examples"):
    time.sleep(1)
```

!!! NOTE
    ```sh
    2038-01-19 03:14:07,000 | DEBUG    | examples:__exit__:50 - executed in 1000.000000 ms
    ```
