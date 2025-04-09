# Web Crawler

This project is a web crawler that fetches product URLs from specified domains.

## Requirements

- Python 3.7 or higher
- Virtual environment setup

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd web-crawler
   ```

2. Run the setup script to create a virtual environment and install dependencies:

   ```bash
   ./setup_env.sh
   ```

3. Activate the virtual environment:
   - On macOS/Linux:

     ```bash
     source .venv/bin/activate
     ```

   - On Windows:

     ```bash
     .venv\Scripts\activate
     ```

4. Run the crawler:

   ```bash
   python -m crawler.main
   ```

## Dependencies

The project uses the following Python libraries:

- `selenium`
- `beautifulsoup4`

Refer to `requirements.txt` for the complete list of dependencies.

## Running Unit Tests

To run the unit tests, use the following command:

```bash
python -m unittest tests/test_crawler.py
```

You can also specify a particular test method to run:

```bash
python -m unittest tests.test_crawler.TestCrawler.test_crawl_virgio
```
