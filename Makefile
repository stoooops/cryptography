DOCKERFILE=Dockerfile
DOCKER_TAG=cryptography
DOCKER_IMAGE=cryptography:latest

PWD=$(shell pwd)
UID=$(shell id -u)
GID=$(shell id -g)

all: build run

build:
	docker build -f $(DOCKERFILE) -t $(DOCKER_TAG) .

run:
	docker run --rm -v $(PWD):/app --user $(UID):$(GID) -t $(DOCKER_TAG) python -m src.main

lint: build
	docker run --rm -v $(PWD):/app --user $(UID):$(GID) -t $(DOCKER_TAG) python -m isort --ignore-whitespace .
	docker run --rm -v $(PWD):/app --user $(UID):$(GID) -t $(DOCKER_TAG) python -m black .
	docker run --rm -v $(PWD):/app --user $(UID):$(GID) -t $(DOCKER_TAG) python -m flake8 .
