.PHONY: all
all:

.PHONY: setup
## setup: Install required tools
setup:
	@echo "Installing..."
	@command -v netlify || npm install --global netlify-cli
	@command -v pelican || pip install --requirement requirements.txt

.PHONY: build
## build: Generate using production settings
build:
	@echo "Rendering..."
	@pelican ./content -o ./output -s ./publishconf.py -t ./themes/resume

.PHONY: pdf
## pdf: Build PDF
pdf:
	@cd $(shell dirname $T) ; latex -output-format=pdf -output-dir=../pdf $(shell basename $T) > /dev/null

.PHONY: serve
## serve: Serve content on port 8000
serve:
	@echo "Serving..."
	@pelican -l ./content -o ./output -s ./pelicanconf.py -t ./themes/resume -b 0.0.0.0

.PHONY: deploy
## deploy: Deploy to Netlify
deploy:
	@echo "Uploading..."
	@netlify deploy --dir=output --prod --build

.PHONY: clean
## clean: Remove generated files
clean:
	@[ ! -d ./output ] || rm -rf ./output

.PHONY: help
## help: Prints this help message
help:
	@echo -e "Usage: \n"
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' |  sed -e 's/^/ /'
