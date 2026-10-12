# FizzBuzz API

A REST API that generates FizzBuzz sequences with statistics tracking.

## What is FizzBuzz?

FizzBuzz is a programming challenge where multiples of specific numbers are replaced with words:
- Multiples of `int1` → replaced with `str1`
- Multiples of `int2` → replaced with `str2`
- Multiples of both → replaced with `str1str2`

## Prerequisites

- Docker
- Poetry (for local development)
- Python 3.13+

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
# Run help command
make help
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

## Concurrency & Scaling

- **Threading model**: Endpoints are sync `def`, so FastAPI runs them in a thread pool (default 40 threads) → up to 40 concurrent requests per process.
- **GIL limit**: FizzBuzz generation is CPU-bound pure Python, so threads interleave rather than run truly parallel. For real CPU parallelism, we need worker processes.
- **Multi-worker caveat**: The in-memory stats store is per-process. With multiple workers each process counts its own hits, we should use shared storage (Redis/DB) later.

## Future Improvements

- Shared managed storage (Redis/DB) for multi-worker or multi-replica deployments (in-memory store is per-process)
- Caching
- Async routes (if database or any I/O added)
- Add pre-commit hooks for linting and formatting
