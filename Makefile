# Makefile

PACKAGE_NAME = docstring2md
PACKAGE_DIR = docstring2md
MAKE := $(MAKE) --no-print-directory
SHELL = bash

default:
	@echo "Makefile for $(PACKAGE_NAME)"
	@echo
	@echo 'Usage:'
	@echo
	@echo '    make install    install the packages' 
	@echo '    make clean      remove the package'
	@echo '    make test       test'
	@echo

install:
	@./setup.py install

clean:
	@rm -Rf *.egg *.egg-info .cache .coverage .tox build dist docs/build htmlcov
	@find -depth -type d -name __pycache__ -exec rm -Rf {} \;
	@find -type f -name '*.pyc' -delete

release:
	@cp requirements.txt requirements.txt-$(date +"%m-%d-%y-%T")
	@pip3 freeze > requirements.txt$

publish:
	@git add .
	@git commit
	@git push

test:
	@echo 'Pep 8 - in progress...'
	@for python_file in $$(ls $(PACKAGE_DIR)); do echo $$python_file; pep8 $(PACKAGE_DIR)/$$python_file; done
	@echo 'Pep 8 - OK !'
	@pep8 setup.py
	@./setup.py test

.PHONY: default install clean test
