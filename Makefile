# Makefile

PACKAGE_NAME = "docstring2md"
PACKAGE_DIR = $(PACKAGE_NAME)
MAKE := $(MAKE) --no-print-directory
SHELL = bash

default:
	@echo "Makefile for $(PACKAGE_NAME)"
	@echo
	@echo 'Usage:'
	@echo
	@echo '    user : make install                   install the packages'
	@echo '           make uninstall                 remove the package'
	@echo '    dev  : make venv                      install venv'
	@echo '           source venv/bin/activate       activate venv'
	@echo '           make dev                       install as dev'
	@echo '           make doc                       make the README'
	@echo '           make test                      test'
	@echo '           make stubs                     refresh stubs'
	@echo

venv:
	@pip3 install virtualenv --user
	@virtualenv venv

dev:
	@pip3 install -e ".[dev]"

install:
	@pip3 install . --upgrade

uninstall:
	@pip3 uninstall -y $(PACKAGE_NAME)

doc:
	@pyreverse $(PACKAGE_NAME) -ASmy -o mmd -p $(PACKAGE_NAME) -d doc
	@export_docstring2md -p $(PACKAGE_DIR) --output-file README.md -mmd doc/classes_docstring2md.mmd -tml pyproject.toml -td doc/todo.md --private-def --toc

stubs:
	@stubgen src/docstring2md -o stubs

test:
	@stubgen src/docstring2md -o stubs
	@pytest

example:
	@pyreverse json -ASmy -o mmd -d example
	@export_docstring2md -p json --output-file example/README.md -mmd example/classes.mmd --private-def --toc

.PHONY: default init dev install uninstall doc stubs test example
