# Fixed-Size Queue Project

## Overview

This project implements a fixed-size, thread-safe FIFO queue using a circular array. You can interact with the queue 
through both a command-line interface (CLI) and a RESTful API.

## Features
- **Fixed Size**: Pre-allocated memory for a fixed number of elements.
- **FIFO**: First-In-First-Out behavior.
- **Thread-Safe**: Safe for multi-threaded environments.
- **CLI & API Support**: Interact with the queue using the command-line or via HTTP requests through the API.

## Changelog
- **9/1/24**: Added RESTful API for interacting with the queue.

## File Structure
- **`src/`**: Contains the main logic and interface files.
  - `fixed_size_queue.py`: Contains the FixedSizeQueue class implementation
  - `api.py`: REST API interface for the queue.
  - `cli.py`: Command-line interface for interacting with the queue
- **`tests/`**: Unit tests.
  - `test_fixed_size_queue.py`: Tests for the queue's core functionality.
  - `test_api.py`: Tests for API endpoints for the queue operations.
- **`openapi.yaml`**: API specification following the OpenAPI standard.
- **`main.py`**: Entry point to run the queue in CLI or API mode.

## Usage
### Command-Line Interface (CLI)
To interact with the queue through the command line:
1. Run the CLI:
    ```bash
    python main.py --cli
    ```
2. Use commands to add, remove, or view elements in the queue.

### API
You can also interact with the queue through the RESTful API.
1. Run the API:
    ```bash
    python main.py --api
    ```

2. Endpoints
- **`GET /queue`**: Retrieves all elements in the queue.
- **`POST /queue`**: Adds an element to the queue.
- **`DELETE /queue`**: Removes an element from the queue.

For a full API specification, refer to the [API Specification](./api-specification.md).

## Author
- **Ziye Liu**