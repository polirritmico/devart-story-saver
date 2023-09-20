SHELL = /bin/bash

SCRIPT_NAME ?= devart-story-saver
COMMIT_NAME ?= $(shell git rev-parse HEAD | cut -c 1-12)

GREEN = \033[0;32m
NOSTYLE = \033[0m

default:
	@echo -e "$(GREEN)Building Docker image...$(NOSTYLE)"
	@docker build --tag ${SCRIPT_NAME}:${COMMIT_HASH} .
	@echo -e "$(GREEN)Done$(NOSTYLE)"

help:
	@echo "Use 'make' to generate the docker image"
	@echo -e "The resulting image will be called '${SCRIPT_NAME}:LAST_COMMIT'"

