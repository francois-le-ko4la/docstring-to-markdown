# Makefile

PACKAGE_NAME = `sed -n "/^    name='\(.*\)',$$/s//\1/p" setup.py`
PACKAGE_DIR = `sed -n "/^    packages=\['\(.*\)'\],$$/s//\1/p" setup.py`
MAKE := $(MAKE) --no-print-directory
SHELL = bash

default:
	@echo "Makefile for $(PACKAGE_NAME)"
	@echo
	@echo 'Usage:'
	@echo
	@echo '    make install    install the packages'
	@echo '    make uninstall  remove the package'
	@echo '    make clean      clean temp file'
	@echo '    make doc        make the README'
	@echo '    make publish    push the last version on GH'
	@echo '    make test       test'
	@echo

uninstall:
	sudo -H pip3 uninstall -y $(PACKAGE_NAME)

install:
	@sudo ./setup.py install

clean:
	@sudo rm -Rf *.egg *.egg-info .cache .coverage .tox build dist docs/build htmlcov .pytest_cache
	@sudo find -depth -type d -name __pycache__ -exec rm -Rf {} \;
	@sudo find -type f -name '*.pyc' -delete

doc:
	@export_docstring2md.py -i $(PACKAGE_DIR) -o README.md

release:
	@$(MAKE) clean
	@$(MAKE) install
	@$(MAKE) doc

publish:
	@git add .
	@git commit
	@git push

test:
	@sudo ./setup.py test

.PHONY: default install uninstall clean test doc publish
