
# Price Generator Service

This is a Python-based service that generates random stock prices for five predefined companies. It continuously generates random prices for each company at 10-second intervals and logs the results to the console. The service can be run locally or inside a Docker container.

## Features

- Generates random prices between 1 and 5000 for five companies: `dell`, `php`, `gg`, `hello`, and `stocks`.
- Logs stock prices to the console every 10 seconds.
- Graceful shutdown on keyboard interrupt (Ctrl+C).
- Can be run locally or using Docker for easy deployment.

## Requirements

- **Local setup**: Python 3.6+ (with Poetry dependency management).
- **Docker setup**: Docker and Docker Compose.

## Installation

### Running Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/price-generator-service.git
   ```

2. Navigate to the project directory:

   ```bash
   cd price-generator-service
   ```

3. Install the dependencies using [Poetry](https://python-poetry.org/):

   ```bash
   poetry install
   ```

4. Run the service:

   ```bash
   python3 main.py
   ```

The service will log stock prices to the console every 10 seconds.

### Running with Docker

To build and run the service using Docker, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/price-generator-service.git
   ```

2. Navigate to the project directory:

   ```bash
   cd price-generator-service
   ```

3. Build the Docker image:

   ```bash
   docker build -t price-generator-service .
   ```

4. Run the Docker container:

   ```bash
   docker run --rm -it price-generator-service
   ```

   The service will run inside the container, and you will see the logged stock prices every 10 seconds.



- **Base Image**: We are using the official Python 3.12 image.
- **Poetry for Dependency Management**: The project uses Poetry to manage dependencies. We install it, disable virtual environments, and install dependencies directly into the Docker environment.
- **Executable Script**: The script is made executable with `chmod +x`.
- **CMD**: The container runs the `main.py` script when started.

## How It Works

- **Company Names**: A list of five company names (`dell`, `php`, `gg`, `hello`, `stocks`) is predefined in the `COMPANY_NAMES` constant.
- **Random Price Generation**: The `generate_stocks()` function generates a random price between 1 and 5000 for each company using Python’s `random.uniform()` function.
- **Logging**: Prices are logged every 10 seconds using Python's built-in `logging` module.
- **Graceful Shutdown**: The script runs indefinitely in a loop until interrupted via `Ctrl+C`, at which point it handles the exception and shuts down cleanly.

## Customization

You can easily modify the script to add more companies by editing the `COMPANY_NAMES` list:

```python
COMPANY_NAMES: List[str] = ['dell', 'php', 'gg', 'hello', 'stocks', 'new_company']
```

To change the time interval, modify the `time.sleep()` argument inside the `main()` function:

```python
time.sleep(10)  # Adjust the time in seconds
```
