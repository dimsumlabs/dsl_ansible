all: lint

BUILD_DEP+=ansible
BUILD_DEP+=ansible-lint

.PHONY: build_dep
build_dep:
	sudo apt-get -y install $(BUILD_DEP)

.PHONY: lint
lint: lint.yaml lint.ansible

.PHONY: lint.yaml
lint.yaml:
	yamllint --strict .
	# scripts/yamlchecksorted.py

.PHONY: lint.ansible
lint.ansible:
	ansible-lint --offline -f pep8 --nocolor
