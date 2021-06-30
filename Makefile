SHELL := /bin/bash
.PHONY: tests update


lint:
	flake8

test-cli:
	pip install -e .
	senderscore -h

test: lint test-cli
	pytest -v --cov=senderscore

update:
	pip install --upgrade -r requirements-dev.in
	pip install -e .
	pip-compile --upgrade -q --output-file=requirements-dev.txt requirements-dev.in

pip-compile:
	pip-compile -q --output-file=requirements-dev.txt requirements-dev.in

build: clean
	python setup.py sdist bdist_wheel
	twine check dist/*

publish:
	twine upload dist/*

clean:
	-@find ./senderscore -name '__pycache__' -exec rm -rf {} \;
	-@find ./tests -name '__pycache__' -exec rm -rf {} \;
	-@find ./ -name '.pytest_cache' -exec rm -rf {} \;
	-@rm -rf *.egg-info
	-@rm -rf build
	-@rm -rf dist
	-@rm .coverage
