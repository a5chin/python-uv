# uv User Guides on this repository

!!! TIP
    Official documentation for uv is available at [https://docs.astral.sh/uv](https://docs.astral.sh/uv)

## Add Python Libraries
If you want to install Python libraries, run the following command:
```sh
uv add ruff
```

!!! NOTE
    If you want to install a specific version of a Python library, run the following command:
    ```sh
    uv add "ruff==0.8.3"
    ```

!!! NOTE
    If you want to install only in dev, run the following command:
    ```sh
    uv add --dev ruff
    ```

## Remove Python Libraries
```sh
uv remove ruff
```

## Pin Python Version
If you want to pin the Python version, run the following command:
```sh
uv pin python 3.13
```

## Configuration for uv
If you want to configure the uv, visit the [Configuration for uv](../configurations/uv.md) page.
