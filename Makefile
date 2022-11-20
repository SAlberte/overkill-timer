# TARGETS
help: .help			## Print help message.
install: .install	## Install development tools
run: .run			## Run project
build: .build		## Rebuild project
lint: .lint			## lints whole project


.DEFAULT_GOAL := install

.help:
	@echo "SUPPORTED TARGETS:"
	@echo
	@echo install
	@echo run
	@echo build
	@echo lint

.install:
	./scripts/install.sh

.run:
	./scripts/deploy.sh

.build:
	./scripts/rebuild.sh

.lint:
	pre-commit run --all-files