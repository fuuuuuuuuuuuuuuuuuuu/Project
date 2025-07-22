# Advance Programming Final Project

This is the final project for the Advance Programming course. It demonstrates the use of object-oriented programming (OOP), generators, decorators, operator overloading, static/class methods, and unit testing in Python.

## Team Members

- Minh Khoi Pham
- Lingbo Kong

## Overview

This project provides a custom system to read and merge text files. It supports:

- A file reader class that reads lines using a generator
- Line filtering based on keywords
- Operator overloading with `__add__` for merging files
- A separate merger class for combining multiple files
- A color output decorator using ANSI escape codes
- Use of `@property`, `@staticmethod`, and `@classmethod`
- Unit tests using `pytest` and fixtures
- Clean code following best practices

## Project Structure

advance-programming-final/
├── src/
│ ├── file_reader.py
│ ├── file_merger.py
│ └── decorators.py
├── tests/
│ ├── test_reader.py
│ └── test_merger.py
├── requirements.txt
├── Makefile
└── README.md
## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/advance-programming-final.git
cd advance-programming-final
```

2. Set up the virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:

```bash
pip install -r requirements.txt

How to Run Tests
All unit tests are written using pytest. Fixtures are used to generate temporary test files.
