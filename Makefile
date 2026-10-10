.PHONY: lint typecheck test build start stop logs clean help

help:
	@echo "Available targets:"
	@echo "  make lint              - Run linter and formatter (ruff)"
	@echo "  make typecheck         - Run type checker (mypy)"
	@echo "  make test              - Run tests (pytest)"
	@echo "  make test-concurrency  - Run concurrency test"
	@echo "  make build             - Build Docker image"
	@echo "  make start [MODE=...]  - Start app (MODE=local or docker, default: docker)"
	@echo "  make start-docker      - Start in Docker with live reload"
	@echo "  make dev-local         - Start locally with live reload"
	@echo "  make stop              - Stop container"
	@echo "  make logs              - Show container logs"
	@echo "  make clean             - Remove container and image"

lint:
	poetry run ruff check --fix
	poetry run ruff format
	poetry run lint-imports

typecheck:
	poetry run mypy src

test:
	poetry run pytest tests -v

test-concurrency:
	poetry run python scripts/test_concurrency.py

build:
	docker build -t fizzbuzz-api:latest .

start:
	@if [ "$(MODE)" = "local" ]; then \
		$(MAKE) dev-local; \
	else \
		$(MAKE) start-docker; \
	fi

start-docker:
	docker rm -f fizzbuzz-app || true
	docker run -p 8000:8000 -v $(shell pwd)/src:/app/src -e WATCHFILES_FORCE_POLLING=true --name fizzbuzz-app fizzbuzz-api:latest python -m uvicorn --reload --reload-dir /app/src --host 0.0.0.0 src.adapters.inbound.restapi.main:app

dev-local:
	poetry run python -m uvicorn --reload src.adapters.inbound.restapi.main:app

stop:
	docker rm -f fizzbuzz-app || true

logs:
	docker logs -f fizzbuzz-app

clean:
	docker rm -f fizzbuzz-app || true
	docker rmi fizzbuzz-api:latest || true
