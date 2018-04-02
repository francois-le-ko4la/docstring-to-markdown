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
	@sudo ./setup.py install

uninstall:
	@sudo -H pip3 uninstall -y $(PACKAGE_NAME)

clean:
	@$(MAKE) uninstall
	@sudo rm -Rf *.egg *.egg-info .cache .coverage .tox build dist docs/build htmlcov
	@sudo find -depth -type d -name __pycache__ -exec rm -Rf {} \;
	@sudo find -type f -name '*.pyc' -delete

release:
	@$(MAKE) clean
	@$(MAKE) install
	@export_docstring2md.py -i $(PACKAGE_DIR) -o README.md
	#@cp requirements.txt requirements.txt-$(date +"%m-%d-%y-%T")
	#@pip3 freeze > requirements.txt$

publish:
	@git add .
	@git commit
	@git push

test:
	@echo 'Pep 8 - in progress...'
	@for python_file in $$(ls $(PACKAGE_DIR)); do echo $$python_file; pep8 $(PACKAGE_DIR)/$$python_file; done
	@echo 'Pep 8 - OK !'
	@pep8 setup.py
	@sudo ./setup.py test

.PHONY: default install clean test
