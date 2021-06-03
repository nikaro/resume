.PHONY: all
all: help

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
## html: Generate site archive
build: pdf html
	@echo "Building..."
	@mkdir -p public/
	@[ -d themes/$(shell jq .meta.theme resume.json)/assets ] && cp -r themes/$(shell jq .meta.theme resume.json)/assets/* public/
	@tar -C public -cz . > site.tar.gz

.PHONY: watch
## serve: Serve content
watch:
	@echo "Watching..."
	@rg --files . | entr resume export --html

.PHONY: serve
## serve: Serve content
serve:
	@echo "Serving..."
	@resume serve

.PHONY: deploy
## deploy: Deploy to SourceHut
deploy:
	@echo "Uploading..."
	@curl --oauth2-bearer "${ACCESS_TOKEN}" -F content=@site.tar.gz https://pages.sr.ht/publish/cv.karolak.fr

.PHONY: clean
## clean: Remove generated files
clean:
	@[ ! -d ./public ] || rm -rf ./public
	@[ ! -f ./site.tar.gz ] || rm -rf ./site.tar.gz

.PHONY: help
## help: Prints this help message
help:
	@echo -e "Usage: \n"
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' |  sed -e 's/^/ /'
