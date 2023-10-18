all: default

default: clean dev_deps deps test clean lint build

all_but_tests: clean dev_deps deps clean lint build

.venv:
	pipenv --venv || pipenv --python 3.7

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr dist/
	rm -fr libs/
	rm -fr src/tests/lrfdt/deps

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

deps: .venv
	pipenv install && pipenv requirements --hash > requirements.txt && pipenv run pip install --upgrade -r requirements.txt -t ./libs && rm requirements.txt

dev_deps: .venv
	pipenv install --dev

check-format: dev_deps
	pipenv run yapf -rd src

format: dev_deps
	 pipenv run yapf -ri src

lint: check-format
	pipenv run pylint -r n src

test: build dev_deps
	pipenv run python -m pytest -v

build: clean deps

console: deps
	pipenv run python

jupyter: deps dev_deps
	pipenv run install-jupyter
	pipenv run jupyter notebook
