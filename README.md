# Advanced Programming Final Project

This final exam project for the Advanced Programming course demonstrates key Python concepts and best practices through a file-reading and merging tool.

## Team Members

- Minh Khoi Pham
- Kong Lingbo

## Features

- **Generator-based file reading**: Reads lines one at a time to handle large files efficiently.
- **Line filtering**: Uses list comprehensions to return only lines containing a given keyword.
- **Operator overloading**: Implements `__add__` so you can merge two `CustomFileReader` instances with `reader1 + reader2`.
- **Inheritance & multi-file merging**: `CustomFileMerger` extends `CustomFileReader` and adds `concat_multiple()` to merge any number of files.
- **ANSI color decorator**: `@deco(color)` adds colored output to demonstration methods without external packages.
- **OOP practices**: Uses `@property` for getters/setters, `@staticmethod` for utilities, and `@classmethod` as a named constructor.
- **Unit testing**: Pytest tests with fixtures ensure each feature works correctly.
- **Continuous Integration**: GitHub Actions runs tests on every push (CI pipeline).

## Project Structure
```plaintext
Project/
├── src/
│   ├── utils.py          # ANSI color decorator
│   ├── file_reader.py    # CustomFileReader class
│   └── file_merger.py    # CustomFileMerger subclass
├── tests/
│   └── test_file_reader.py  # Pytest tests for all features
├── requirements.txt      # Project dependencies
├── Makefile              # Commands: make test, make clean
├── .github/
│   └── workflows/
│       └── python-tests.yml  # GitHub Actions CI config
└── README.md             # Project documentation
```

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/advanced-programming-final.git
   cd advanced-programming-final
   ```

2. **Create and activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   # venv\Scripts\activate   # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

* **Merge two files:**

  ```python
  from src.file_reader import CustomFileReader
  r1 = CustomFileReader('file1.txt')
  r2 = CustomFileReader('file2.txt')
  merged = r1 + r2
  print(merged.filepath)  # e.g. 'merged_file1_file2.txt'
  ```

* **Merge multiple files:**

  ```python
  from src.file_merger import CustomFileMerger
  merger = CustomFileMerger('file1.txt')
  result = merger.concat_multiple(r2, r3, r4)
  print(result.filepath)
  ```

* **Filter lines and display in color:**

  ```python
  from src.file_reader import CustomFileReader
  reader = CustomFileReader('file.txt')
  print(reader.display_lines_with_keyword('error'))
  ```

## Running Tests

* **Locally:**

  ```bash
  make test
  ```

* **CI:**

  GitHub Actions will automatically run tests on every push. Check the [Actions tab](../../actions) in the repository.

## Clean-up

* **Remove compiled files:**

  ```bash
  make clean
  ```

## Docstrings

All classes and methods include docstrings for clarity and maintainability.