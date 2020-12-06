.PHONY: all
all: help

.PHONY: setup
## setup: Install required tools
setup:
	@echo "Installing..."
	@command -v resumepy || pip install resume-pycli

.PHONY: build
## build: Generate outputs
build:
	@echo "Rendering..."
	@resume validate --schema schema.json
	@resume export
	@tar -C public -cvz . > site.tar.gz

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
