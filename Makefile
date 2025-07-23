.PHONY: test lint clean

test:
	PYTHONPATH=src pytest

test-file:
	PYTHONPATH=src pytest $(f)

lint:
	flake8 src tests

clean:
	find . -type f -name "*.pyc" -delete
