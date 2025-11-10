# Tracer - Performance Monitoring

The Tracer module provides a simple Timer utility for measuring and logging code execution time. It works as both a decorator and a context manager, making it easy to monitor performance in any part of your application.

## Overview

The Timer class offers:

- **Dual usage** - Works as decorator or context manager
- **Automatic logging** - Execution time logged automatically
- **Millisecond precision** - Accurate timing measurements
- **Zero boilerplate** - No manual time tracking needed
- **Logger integration** - Uses the built-in Logger module

## Basic Usage

### As a Context Manager

Use `with Timer()` to measure a block of code:

```python
import time
from tools.tracer import Timer

with Timer("database_query"):
    time.sleep(1)  # Simulate database query
```

**Output:**
```
2038-01-19 03:14:07,000 | DEBUG | database_query:__exit__:50 - executed in 1000.000000 ms
```

### As a Decorator

Use `@Timer()` to measure function execution:

```python
import time
from tools.tracer import Timer

@Timer("process_data")
def process_data(data):
    time.sleep(1)  # Simulate processing
    return data

result = process_data([1, 2, 3])
```

**Output:**
```
2038-01-19 03:14:07,000 | DEBUG | process_data:__exit__:50 - executed in 1000.000000 ms
```

## Real-World Examples

### API Endpoint Monitoring

Monitor API endpoint performance:

```python
from fastapi import FastAPI
from tools.tracer import Timer

app = FastAPI()

@app.get("/users/{user_id}")
@Timer("get_user_endpoint")
async def get_user(user_id: int):
    with Timer("database_lookup"):
        user = await db.get_user(user_id)

    with Timer("user_serialization"):
        return user.dict()
```

**Output:**
```
2038-01-19 03:14:07,000 | DEBUG | database_lookup:__exit__:50 - executed in 45.123000 ms
2038-01-19 03:14:07,100 | DEBUG | user_serialization:__exit__:50 - executed in 2.456000 ms
2038-01-19 03:14:07,150 | DEBUG | get_user_endpoint:__exit__:50 - executed in 50.789000 ms
```

### Data Processing Pipeline

Monitor each stage of a data pipeline:

```python
from tools.tracer import Timer
from tools.logger import Logger

logger = Logger(__name__)

@Timer("full_pipeline")
def process_dataset(data):
    logger.info(f"Processing {len(data)} records")

    with Timer("data_validation"):
        validated = validate_data(data)

    with Timer("data_transformation"):
        transformed = transform_data(validated)

    with Timer("data_enrichment"):
        enriched = enrich_data(transformed)

    with Timer("data_storage"):
        save_data(enriched)

    logger.info("Pipeline complete")
    return enriched
```

### Database Operations

Monitor individual database operations:

```python
from sqlalchemy.orm import Session
from tools.tracer import Timer

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    @Timer("user_create")
    def create_user(self, user_data: dict):
        user = User(**user_data)
        self.db.add(user)
        self.db.commit()
        return user

    @Timer("user_bulk_import")
    def import_users(self, users_data: list[dict]):
        with Timer("user_validation"):
            validated = [validate(u) for u in users_data]

        with Timer("user_db_insert"):
            self.db.bulk_insert_mappings(User, validated)
            self.db.commit()
```

### File Processing

Track file I/O operations:

```python
import json
from tools.tracer import Timer

@Timer("process_json_file")
def process_json_file(filepath: str):
    with Timer("file_read"):
        with open(filepath, 'r') as f:
            data = json.load(f)

    with Timer("data_processing"):
        processed = transform(data)

    with Timer("file_write"):
        with open(f"{filepath}.processed", 'w') as f:
            json.dump(processed, f)

    return processed
```

## Nested Timers

You can nest timers to measure both overall and component timings:

```python
from tools.tracer import Timer

@Timer("complete_analysis")
def analyze_data(dataset):
    with Timer("load_models"):
        model_a = load_model_a()
        model_b = load_model_b()

    with Timer("run_models"):
        with Timer("model_a_inference"):
            results_a = model_a.predict(dataset)

        with Timer("model_b_inference"):
            results_b = model_b.predict(dataset)

    with Timer("combine_results"):
        final = combine(results_a, results_b)

    return final
```

**Output:**
```
2038-01-19 03:14:07,000 | DEBUG | load_models:__exit__:50 - executed in 500.000000 ms
2038-01-19 03:14:07,550 | DEBUG | model_a_inference:__exit__:50 - executed in 120.000000 ms
2038-01-19 03:14:07,700 | DEBUG | model_b_inference:__exit__:50 - executed in 130.000000 ms
2038-01-19 03:14:07,850 | DEBUG | run_models:__exit__:50 - executed in 250.000000 ms
2038-01-19 03:14:07,900 | DEBUG | combine_results:__exit__:50 - executed in 50.000000 ms
2038-01-19 03:14:07,950 | DEBUG | complete_analysis:__exit__:50 - executed in 800.000000 ms
```

## Integration with Logging

The Timer automatically uses the Logger module. You can combine them for comprehensive monitoring:

```python
from tools.logger import Logger
from tools.tracer import Timer

logger = Logger(__name__)

@Timer("expensive_operation")
def expensive_operation(items: list):
    logger.info(f"Starting operation with {len(items)} items")

    with Timer("preprocessing"):
        preprocessed = preprocess(items)
        logger.debug(f"Preprocessed {len(preprocessed)} items")

    with Timer("main_processing"):
        results = process(preprocessed)
        logger.debug(f"Processed into {len(results)} results")

    logger.info("Operation complete")
    return results
```

## Best Practices

### 1. Meaningful Timer Names

Use descriptive names that clearly indicate what's being measured:

```python
# Good
with Timer("database_user_query"):
    user = db.query(User).filter_by(id=user_id).first()

# Less useful
with Timer("query"):
    user = db.query(User).filter_by(id=user_id).first()
```

### 2. Measure at Appropriate Granularity

Don't time trivial operations - focus on operations that matter:

```python
# Good - measures significant operations
@Timer("process_large_dataset")
def process_dataset(data):
    return [transform(item) for item in data]

# Too granular - overhead not worth it
for item in data:
    with Timer("process_single_item"):  # Too fine-grained
        process(item)
```

### 3. Use Consistent Naming

Establish naming conventions for different operation types:

```python
# Database operations
with Timer("db_query_users"):
    users = db.query(User).all()

# API calls
with Timer("api_call_external_service"):
    response = requests.get(url)

# File operations
with Timer("file_read_config"):
    config = load_config()
```

### 4. Combine with Monitoring

Use Timer data for performance monitoring and optimization:

```python
from tools.tracer import Timer
from tools.logger import Logger

logger = Logger(__name__)

SLOW_QUERY_THRESHOLD_MS = 1000

@Timer("database_query")
def query_users(filters):
    start = time.time()

    with Timer("db_execution"):
        results = db.query(User).filter(**filters).all()

    duration_ms = (time.time() - start) * 1000

    if duration_ms > SLOW_QUERY_THRESHOLD_MS:
        logger.warning(f"Slow query detected: {duration_ms:.2f}ms")

    return results
```

## Implementation Details

The Timer class is built using Python's `ContextDecorator`, which allows it to work as both a context manager and a decorator.

### How It Works

1. **`__enter__`**: Records start time
2. **Code execution**: Your code runs
3. **`__exit__`**: Calculates duration and logs it

The duration is automatically logged using the Logger module at `DEBUG` level.

## Advanced Usage

### Custom Timer Subclass

Extend Timer to add custom behavior:

```python
from tools.tracer import Timer
from tools.logger import Logger

class MetricsTimer(Timer):
    """Timer that also records metrics to a metrics system."""

    def __exit__(self, *exc):
        super().__exit__(*exc)

        # Record to metrics system
        metrics.record_timing(self.name, self._duration * 1000)

# Usage
with MetricsTimer("api_call"):
    response = call_api()
```

### Conditional Timing

Enable timing based on configuration:

```python
from contextlib import nullcontext
from tools.config import Settings
from tools.tracer import Timer

settings = Settings()

def maybe_timer(name: str):
    """Return Timer if profiling is enabled, else no-op."""
    if settings.ENABLE_PROFILING:
        return Timer(name)
    return nullcontext()

# Usage
with maybe_timer("optional_timing"):
    process_data()
```

## Testing

Test code with timers by checking log output:

```python
import logging
from tools.tracer import Timer

def test_timer_logging():
    with assertLogs(level=logging.DEBUG) as cm:
        with Timer("test_operation"):
            pass  # Instant operation

    assert "test_operation" in cm.output[0]
    assert "executed in" in cm.output[0]
    assert "ms" in cm.output[0]
```

## Related Documentation

- [Logger Guide](logger.md) - Understanding the logging output
- [FastAPI Use Case](../../usecases/fastapi.md) - Timer in web applications
- [Configuration Guide](config.md) - Configure timing behavior
