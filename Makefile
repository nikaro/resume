.PHONY: all
all: build

# curl -sL <URL> | openssl dgst -sha384 -binary | openssl base64 -A

.PHONY: setup
## setup: Install required tools
setup:
	@echo "Installing..."
	command -v goresume || GOBIN=$(shell go env GOROOT)/bin go install github.com/nikaro/goresume@latest
	
.PHONY: validate
## validate: Validate JSON
validate:
	@echo "Checking..."
	goresume validate --resume resume.yaml --schema schema.json

.PHONY: pdf
## pdf: Generate PDF
pdf:
	@echo "Rendering PDF..."
	goresume export --resume resume.yaml --html=false

.PHONY: html
## html: Generate HTML
html:
	@echo "Rendering HTML..."
	goresume export --resume resume.yaml --pdf=false

.PHONY: build
## build: Generate HTML and PDF
build:
	@echo "Building..."
	mkdir -p public
	goresume export --resume resume.yaml --log-level info

.PHONY: serve
## serve: Start a local HTTP server
serve:
	@echo "Serving..."
	python -m http.server --directory public --bind localhost

.PHONY: watch
## watch: Live-update resume on changes
watch:
	@echo "Watching..."
	rg --files . | entr resume export --resume resume.yaml

.PHONY: clean
## clean: Remove generated files
clean:
	@echo "Cleaning..."
	rm -rf ./public

.PHONY: help
## help: Prints this help message
help:
	@echo "Usage: \n"
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' |  sed -e 's/^/ /'
