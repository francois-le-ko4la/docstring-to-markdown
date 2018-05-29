# Makefile

PACKAGE_NAME = `sudo ./setup.py --name`
PACKAGE_DIR = $(PACKAGE_NAME)
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

dev:
	@sudo -H pip3 install -e .

install:
	@./setup.py sdist bdist_wheel
	@sudo -H pip3 install . --upgrade

upgrade:
	@sudo -H pip3 install . --upgrade

uninstall:
	@sudo -H pip3 uninstall -y $(PACKAGE_NAME)

clean:
	@sudo rm -Rf .eggs *.egg-info .cache .coverage .tox build dist docs/build htmlcov .pytest_cache
	@sudo find -depth -type d -name __pycache__ -exec rm -Rf {} \;
	@sudo find -type f -name '*.pyc' -delete

fulldoc:
	@pyreverse $(PACKAGE_NAME) -f ALL -o png -p $(PACKAGE_NAME)
	@mv *.png pictures/
	@$(MAKE) doc

doc:
	@export_docstring2md.py -i $(PACKAGE_DIR) -o README.md -r requirements.txt -t runtime.txt -u pictures/classes_$(PACKAGE_NAME).png

release:
	@$(MAKE) clean
	@$(MAKE) install
	@$(MAKE) doc

publish:
	@$(MAKE) test
	@git add .
	@git commit
	@git push

test:
	@pip3 show $(PACKAGE_NAME)
	@sudo ./setup.py test
	@sudo ./setup.py test > last_check.log

.PHONY: default init dev install uninstall clean test doc publish release
