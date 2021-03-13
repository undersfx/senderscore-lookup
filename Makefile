SHELL := /bin/bash
.PHONY: tests

lint:
	@echo ">>> Running lints"
	@flake8

test: lint
	@echo ">>> Running tests"
	@pytest -v --cov=senderscore

setup:
	pip install -r requirements-dev.txt
	pip install -e .

build:
	python setup.py sdist bdist_wheel
	twine check dist/*

publish:
	twine upload dist/*