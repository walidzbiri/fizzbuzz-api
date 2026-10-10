# FizzBuzz API

A REST API that generates FizzBuzz sequences.

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
│   └── exceptions.py         # Exceptions
└── adapters/
    └── inbound/restapi/v1/   # HTTP endpoints
```

## Design Decisions

- **Immutable Value Objects**: FizzBuzzParams is a frozen dataclass
- **Hexagonal Architecture**: Business logic independent of frameworks

## Future Improvements

- Statistics endpoint tracking most frequent request
- Database adapter for persistence
- Rate limiting
- Caching
