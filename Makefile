SHELL := /bin/bash
.PHONY: tests


lint:
	flake8

test: lint
	pytest -v --cov=senderscore

update:
	pip install --upgrade -r requirements-dev.in
	pip install --upgrade -r requirements.in
	pip install -e .

pip-compile:
	pip-compile -q --upgrade --generate-hashes --output-file=requirements-dev.txt requirements-dev.in
	pip-compile -q --upgrade --generate-hashes --output-file=requirements.txt requirements.in

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
