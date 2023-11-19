### English

# ZIP Brute Force Tool

Welcome to the `zip_bruteforce_tool` project. This professional-grade Python tool is designed to perform brute force attacks on password-protected ZIP archives using powerful tools like John the Ripper and fcrackzip.

## Features
- Perform brute force attacks on ZIP files
- Leverage John the Ripper and fcrackzip for efficient password cracking
- Comprehensive scripts and utilities for generating test archives and running attacks
- Easy to extend and customize

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Tom-Souillard/zip_bruteforce_tool.git
    cd zip_bruteforce_tool
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Install fcrackzip and John the Ripper:
    ```bash
    sudo apt-get install fcrackzip john
    ```

## Usage

### Generate Test Archives

Generate a test ZIP archive with a known password:
```bash
python scripts/generate_test_archives.py
```

### Run Brute Force Attack with fcrackzip

```bash
python scripts/run_fcrackzip.py path/to/your/test.zip
```

### Run Brute Force Attack with John the Ripper

First, extract the hash from the ZIP file:
```bash
python scripts/extract_zip_hash.py path/to/your/test.zip
```

Then, run John the Ripper:
```bash
python scripts/run_john.py zip_hash.txt
```

## Testing

Run unit tests to ensure the tool works correctly:
```bash
pytest
```

## Documentation

For detailed usage and customization instructions, please refer to the [documentation](docs/README.md).

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING](CONTRIBUTING.md) guidelines before submitting a pull request.

---