# Advance Programming Final Project

This is the final project for the Advance Programming course. It demonstrates the use of object-oriented programming, generators, decorators, special methods, and testing in Python.

## Team Members

- Philip  
- Lingbo

## Overview

The project implements a custom file reading and merging system. It includes:

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

2. Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install dependencies:

pip install -r requirements.txt

How to Run Tests
All unit tests are written using pytest. Fixtures are used to generate temporary test files.
