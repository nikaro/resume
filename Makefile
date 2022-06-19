.PHONY: all
all: help

# openssl dgst -sha384 -binary FILENAME.js | openssl base64 -A

.PHONY: setup
## setup: Install required tools
setup:
	@echo "Installing..."
	@command -v resumepy || pip install resume-pycli

.PHONY: validate
## validate: Validate JSON
validate:
	@echo "Checking..."
	@resume validate --schema schema.json

.PHONY: pdf
## pdf: Generate PDF
pdf: validate
	@echo "Rendering PDF..."
	@resume export --pdf --theme stackoverflow

.PHONY: html
## html: Generate HTML
html: validate
	@echo "Rendering HTML..."
	@resume export --html

.PHONY: build
## build: Generate site archive
build: pdf html
	@echo "Building..."
	@mkdir -p public/
	@[ -d themes/$(shell jq .meta.theme resume.json)/assets ] && cp -r themes/$(shell jq .meta.theme resume.json)/assets public/

.PHONY: watch
## watch: Live-update resume on changes
watch:
	@echo "Watching..."
	@rg --files . | entr resume export --html

.PHONY: serve
## serve: Serve content
serve:
	@echo "Serving..."
	@resume serve --bind 0.0.0.0

.PHONY: clean
## clean: Remove generated files
clean:
	@[ ! -d ./public ] || rm -rf ./public

.PHONY: help
## help: Prints this help message
help:
	@echo "Usage: \n"
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' |  sed -e 's/^/ /'
