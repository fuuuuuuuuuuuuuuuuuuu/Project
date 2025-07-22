.PHONY: test lint clean

test:
	PYTHONPATH=src pytest

lint:
	flake8 src tests

clean:
	find . -type f -name "*.pyc" -delete
