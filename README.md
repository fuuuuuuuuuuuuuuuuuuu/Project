# Advance Programming Final Project

This is the final project for the Advance Programming course. It demonstrates the use of object-oriented programming (OOP), generators, decorators, operator overloading, static/class methods, and unit testing in Python.

## Team Members

- Minh Khoi Pham
- Lingbo Kong

## Overview

This project provides a custom system to read and merge text files. It supports:

- Lazy reading of files using generators
- Filtering lines by keyword
- Operator overloading with `__add__` for merging two files
- Merging multiple files via a `CustomFileMerger` class
- Use of `@property`, `@staticmethod`, and `@classmethod`
- ANSI color decorator with no third-party libraries
- Unit tests using `pytest` and fixtures
- Clean, modular, testable codebase

## Project Structure

```
project-root/
├── src/
│   ├── file_reader.py         # CustomFileReader class
│   ├── file_merger.py         # Inherits from CustomFileReader, supports multi-file merging
│   └── utils.py               # color decorator implementation
├── tests/
│   └── test_file_reader.py    # Pytest test cases
├── .gitignore
├── LICENSE
├── Makefile
├── Project.code-workspace
├── README.md
├── requirements.txt
├── test_run.py               # Manual demo/test script
├── sample.txt
├── sample2.txt
├── new_file.txt
├── merged_sample_another.txt
├── merged_sample_sample2.txt
└── merged_multi_sample.txt
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/advance-programming-final.git
cd advance-programming-final
```

2. Set up the virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

Tests are located in the `tests/` directory. Use `pytest` to run all tests:

```bash
pytest
```

Fixtures are used to generate isolated temporary files for test safety.

## Example Usage (from `test_run.py`)

```python
from src.file_reader import CustomFileReader
from src.file_merger import CustomFileMerger
from src.utils import deco

# Read file
r1 = CustomFileReader("sample.txt")
for line in r1.line_generator():
    print(line.strip())

# Merge files using + operator
r2 = CustomFileReader("sample2.txt")
merged = r1 + r2

# Merge multiple files
merger = CustomFileMerger("sample.txt")
merged_all = merger.concat_multiple(r2)

# Colored output using decorator
@deco("green")
def success():
    return "All tests passed!"

print(success())
```

## Decorator Notes

The `@deco(color)` decorator is defined in `utils.py`. It adds ANSI color codes to terminal output based on the given color name. No external libraries are used.

## Makefile Commands (if applicable)

```make
make test        # run pytest
make clean       # remove .pyc and __pycache__
```

## License

This project is released under the MIT License. See LICENSE for details.

## Presentation

- Date: July 24, 2025
- Format: In-class presentation
- Topics: OOP, decorators, testing, file handling, CI-ready Python project

