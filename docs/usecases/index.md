# Use Cases

This section demonstrates how to use this template for real-world projects. Each use case shows practical examples of integrating the tools and utilities for specific types of applications.

## Overview

This template is versatile and can be adapted for various Python projects:

- **Web APIs** - FastAPI applications with logging and configuration
- **Data Science** - Jupyter notebooks with proper dependency management
- **Computer Vision** - OpenCV projects with performance monitoring
- **Microservices** - Production-ready services with structured logging
- **Data Pipelines** - ETL processes with performance tracking
- **CLI Tools** - Command-line applications with configuration management

## Featured Use Cases

### [Jupyter Notebooks](jupyter.md)

Learn how to use Jupyter notebooks in this environment for data science and exploratory work.

**What you'll learn:**

- Setting up Jupyter with the Dev Container
- Managing notebook dependencies with uv
- Using the built-in utilities in notebooks
- Combining notebooks with production code

**Perfect for:**
- Data exploration and analysis
- Machine learning experimentation
- Creating reproducible research
- Prototyping algorithms

**Key features demonstrated:**

```python
# Use the Logger in notebooks
from tools.logger import Logger
logger = Logger(__name__)
logger.info("Starting analysis")

# Time expensive operations
from tools.tracer import Timer
with Timer("data_loading"):
    df = pd.read_csv("large_dataset.csv")
```

[→ Read the full Jupyter use case](jupyter.md)

---

### [FastAPI Applications](fastapi.md)

Build production-ready web APIs using FastAPI with the template's configuration and logging utilities.

**What you'll learn:**

- Integrating Settings for API configuration
- Structured logging for API endpoints
- Performance monitoring with Timer
- Environment-based configuration (local vs production)
- Database integration patterns

**Perfect for:**
- REST APIs
- Microservices
- Backend services
- Real-time applications

**Key features demonstrated:**

```python
from fastapi import FastAPI
from tools.config import Settings
from tools.logger import Logger, LogType

settings = Settings()
logger = Logger(__name__,
    log_type=LogType.LOCAL if settings.IS_LOCAL else LogType.GOOGLE_CLOUD
)

app = FastAPI(**settings.fastapi_kwargs)

@app.get("/")
@Timer("root_endpoint")
async def root():
    logger.info("Root endpoint accessed")
    return {"status": "healthy"}
```

[→ Read the full FastAPI use case](fastapi.md)

---

### [OpenCV Projects](opencv.md)

Build computer vision applications with OpenCV, using the template's utilities for performance monitoring.

**What you'll learn:**

- Setting up OpenCV in the Dev Container
- Managing computer vision dependencies
- Performance monitoring for image processing
- Logging for debugging vision pipelines

**Perfect for:**
- Image processing applications
- Video analysis
- Real-time computer vision
- Machine learning pipelines

**Key features demonstrated:**

```python
import cv2
from tools.tracer import Timer
from tools.logger import Logger

logger = Logger(__name__)

@Timer("image_processing")
def process_image(image_path: str):
    with Timer("image_read"):
        image = cv2.imread(image_path)
        logger.info(f"Loaded image: {image.shape}")

    with Timer("preprocessing"):
        processed = preprocess(image)

    with Timer("detection"):
        results = detect_objects(processed)
        logger.info(f"Found {len(results)} objects")

    return results
```

[→ Read the full OpenCV use case](opencv.md)

## Additional Use Case Ideas

### Data Pipeline Example

```python
from tools.logger import Logger
from tools.tracer import Timer
from tools.config import Settings

logger = Logger(__name__)
settings = Settings()

@Timer("etl_pipeline")
def run_etl():
    logger.info("Starting ETL pipeline")

    with Timer("extract"):
        data = extract_from_source(settings.DATA_SOURCE_URL)
        logger.info(f"Extracted {len(data)} records")

    with Timer("transform"):
        transformed = transform_data(data)
        logger.debug(f"Transformation complete")

    with Timer("load"):
        load_to_warehouse(transformed, settings.WAREHOUSE_URL)
        logger.info(f"Loaded {len(transformed)} records")
```

### CLI Application Example

```python
import typer
from tools.config import Settings
from tools.logger import Logger
from tools.tracer import Timer

app = typer.Typer()
settings = Settings()
logger = Logger(__name__)

@app.command()
@Timer("process_command")
def process(
    input_file: str,
    output_file: str,
    verbose: bool = False
):
    """Process input file and write results."""
    if verbose:
        logger.info(f"Processing {input_file}")

    with Timer("file_processing"):
        result = process_file(input_file)

    with Timer("file_write"):
        write_output(result, output_file)

    logger.info("Processing complete")

if __name__ == "__main__":
    app()
```

### Batch Processing Example

```python
from concurrent.futures import ThreadPoolExecutor
from tools.logger import Logger
from tools.tracer import Timer

logger = Logger(__name__)

@Timer("batch_processor")
def process_batch(items: list):
    logger.info(f"Processing batch of {len(items)} items")

    with Timer("parallel_processing"):
        with ThreadPoolExecutor(max_workers=4) as executor:
            results = list(executor.map(process_item, items))

    logger.info(f"Processed {len(results)} items")
    return results

@Timer("item_processing")
def process_item(item):
    # Process individual item
    return transform(item)
```

## Combining Use Cases

You can combine patterns from different use cases. For example:

**Web API + Data Processing:**
```python
from fastapi import FastAPI, BackgroundTasks
from tools.config import Settings
from tools.logger import Logger, LogType
from tools.tracer import Timer

settings = Settings()
logger = Logger(__name__,
    log_type=LogType.LOCAL if settings.IS_LOCAL else LogType.GOOGLE_CLOUD
)

app = FastAPI(**settings.fastapi_kwargs)

@app.post("/process")
@Timer("process_endpoint")
async def process_data(
    data: list,
    background_tasks: BackgroundTasks
):
    logger.info(f"Received {len(data)} items for processing")

    # Process in background
    background_tasks.add_task(process_batch, data)

    return {"status": "processing", "items": len(data)}
```

## Getting Started with Use Cases

1. **Choose your use case** - Pick the one closest to your project type
2. **Read the guide** - Follow the step-by-step instructions
3. **Adapt to your needs** - Modify the examples for your specific requirements
4. **Explore the code** - Check the complete examples in each guide

## Best Practices Across All Use Cases

### 1. Use Environment-Based Configuration

Always configure based on environment:

```python
from tools.config import Settings
from tools.logger import Logger, LogType

settings = Settings()
logger = Logger(
    __name__,
    log_type=LogType.LOCAL if settings.IS_LOCAL else LogType.GOOGLE_CLOUD
)
```

### 2. Monitor Performance

Use Timer for critical operations:

```python
from tools.tracer import Timer

@Timer("critical_operation")
def critical_operation():
    # Your code here
    pass
```

### 3. Structured Logging

Include context in log messages:

```python
logger.info(f"Processing user {user_id}: {action}")  # Good
logger.info("Processing")  # Less useful
```

### 4. Type Hints

Leverage type checking for better code quality:

```python
from typing import list

def process_items(items: list[dict]) -> list[Result]:
    return [process(item) for item in items]
```

### 5. Test Your Code

Write tests for your use case:

```python
def test_process_data():
    result = process_data([1, 2, 3])
    assert len(result) == 3
```

## Next Steps

- **Explore a use case**: Pick one and follow the detailed guide
- **Review the tools**: Check the [built-in utilities documentation](../guides/tools/index.md)
- **Understand configuration**: Read the [configuration guides](../configurations/index.md)
- **Start building**: Apply the patterns to your own project

## Need More Examples?

- Check the `tests/` directory for test examples
- Review the `tools/` source code for implementation patterns
- Browse the [GitHub repository](https://github.com/a5chin/python-uv) for additional examples
