# Makefile for Express.js application

# Variables
NODE = node
APP = app.js
PORT = 3000

# Default target
.PHONY: all
all: run

# Run the application
.PHONY: run
run:
	$(NODE) $(APP)

# Run with development mode (if you have nodemon installed)
.PHONY: dev
dev:
	npx nodemon $(APP)

# Install dependencies
.PHONY: install
install:
	npm install

# Run tests (if you have a test script in package.json)
.PHONY: test
test:
	npm test

# Start with specific port
.PHONY: start
start:
	PORT=$(PORT) $(NODE) $(APP)

# Clean node_modules and package-lock.json
.PHONY: clean
clean:
	rm -rf node_modules package-lock.json

# Reinstall dependencies
.PHONY: reinstall
reinstall: clean install

# Check if Node.js is installed
.PHONY: check
check:
	@which $(NODE) > /dev/null || (echo "Node.js is not installed" && exit 1)
	@echo "Node.js is installed: $$($(NODE) --version)"
