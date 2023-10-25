all: default

default: clean dev_deps deps test clean lint build

all_but_tests: clean dev_deps deps clean lint build

.venv:
	pipenv --venv || pipenv --python 3.11

clean: 

deps: .venv
	pipenv install

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

python-version:
	pyenv version
	pipenv run python --version	
