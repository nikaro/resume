.PHONY: all
all: help

# openssl dgst -sha384 -binary FILENAME.js | openssl base64 -A

.PHONY: setup
## setup: Install required tools
setup:
	@echo "Installing..."
	poetry install --no-interaction

.PHONY: validate
## validate: Validate JSON
validate:
	@echo "Checking..."
	poetry run resume validate

.PHONY: pdf
## pdf: Generate PDF
pdf: validate
	@echo "Rendering PDF..."
	poetry run resume export --no-html --theme stackoverflow

.PHONY: html
## html: Generate HTML
html: validate
	@echo "Rendering HTML..."
	poetry run resume export --no-pdf

.PHONY: watch
## watch: Live-update resume on changes
watch:
	@echo "Watching..."
	rg --files . | entr poetry run resume export --html

.PHONY: serve
## serve: Serve content
serve:
	@echo "Serving..."
	poetry run resume serve --host 0.0.0.0

.PHONY: build
## build: Build Python package
build: setup pdf html
	@echo "Building package..."
	poetry build --no-interaction

.PHONY: clean
## clean: Remove generated files
clean:
	@echo "Cleaning..."
	rm -rf ./dist
	rm -rf ./public
	poetry env remove --all --no-interaction

.PHONY: publish
## publish: Publish on PyPI
publish:
	@echo "Publishing..."
	poetry publish

.PHONY: help
## help: Prints this help message
help:
	@echo "Usage: \n"
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' |  sed -e 's/^/ /'
