#!make

# Command Variables
D = docker
DC = docker-compose
DCFLAGS = --rm app
PYTHON = python
ifeq (,$(wildcard /.dockerenv))
	PYTHON := $(DC) run $(DCFLAGS) $(PYTHON)
endif

artifacts = \
	.coverage \
	.mypy_cache \
	.pytest_cache

all: install
	@echo "You can now run the engine with `make run`."
.PHONY: all

clean:
	@rm -rf $(artifacts)
	@find . -depth -name '__pycache__' -exec rm -rv {} \;
.PHONY: clean

install:
	@$(PYTHON) -m pip install -r requirements.txt
.PHONY: install

run:
	$(PYTHON) main.py
.PHONY: run
