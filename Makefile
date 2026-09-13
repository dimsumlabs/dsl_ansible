all: lint test

BUILD_DEP+=ansible
BUILD_DEP+=ansible-lint
BUILD_DEP+=flake8
BUILD_DEP+=python3-coverage
BUILD_DEP+=python3-pytest
BUILD_DEP+=python3-pytest-cov

PYFILES=$(shell find -name \*.py)

.PHONY: build_dep
build_dep:
	sudo apt-get -y install $(BUILD_DEP)

.PHONY: lint
lint: lint.yaml lint.schema lint.python lint.ansible

.PHONY: test
test: test.python

.PHONY: lint.yaml
lint.yaml:
	yamllint --strict .
	# scripts/yamlchecksorted.py

.PHONY: lint.ansible
lint.ansible:
	ansible-lint --offline -f pep8 --nocolor

.PHONY: lint.schema
lint.schema:
	roles/users/scripts/lint_userdb.py

.PHONY: lint.python
lint.python:
	flake8

.PHONY: test.python
test.python:
	pytest-3 \
            --cov-report=term-missing \
            --cov-report=html \
            --cov-fail-under=45 \
            --cov=. \
	    $(PYFILES)
