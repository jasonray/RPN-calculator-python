all: default

clean: 

deps:
	python3 -m pip install -r requirements.txt

dev_deps:
	python3 -m pip install -r requirements-dev.txt

check-format: dev_deps
	yapf -rd src

format: dev_deps
	yapf -ri src

lint: check-format
	pylint -r n src

test: build dev_deps
	python3 -m pytest -v

build: clean deps
