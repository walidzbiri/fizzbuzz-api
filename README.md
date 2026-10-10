# FizzBuzz API

A REST API that generates FizzBuzz sequences with statistics tracking.

## What is FizzBuzz?

FizzBuzz is a programming challenge where multiples of specific numbers are replaced with words:
- Multiples of `int1` → replaced with `str1`
- Multiples of `int2` → replaced with `str2`
- Multiples of both → replaced with `str1str2`

## Prerequisites

- Docker

## Quick Start

```bash
# Build image
make build

# Start container
MODE=docker make start
```

Server runs at `http://localhost:8000`

## Try It

```bash
# Generate sequence
curl "http://localhost:8000/api/v1/fizzbuzz?int1=3&int2=5&limit=15&str1=Fizz&str2=Buzz"

# Get statistics
curl "http://localhost:8000/api/v1/stats"
```

## Development

```bash
# Run tests
make test

# Type check
make typecheck

# Lint
make lint

# Format
make format

# Local development (hot reload)
make dev-local
```

## Project Structure

```
src/
├── domain/fizzbuzz/          # Business logic
│   ├── models.py             # Data models
│   ├── service.py            # FizzBuzz logic
│   ├── ports.py              # Interfaces
│   └── exceptions.py         # Exceptions
└── adapters/
    ├── inbound/restapi/v1/   # HTTP endpoints
    └── outbound/             # Data storage
```

## Design Decisions

- **Dependency Injection**: Stats store injected into service
- **In-Memory Storage**: Simple, fast, sufficient for MVP
- **Hexagonal Architecture**: Business logic independent of frameworks

## Future Improvements

- Database adapter for persistent stats
- Shared storage (Redis/DB) for multi-worker or multi-replica deployments (in-memory store is per-process)
- Rate limiting
- Caching
- Async routes (if database or any I/O added)
- Add pre-commit hooks for linting and formatting
