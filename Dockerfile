FROM python:3.13-slim AS builder

ARG MODE

RUN pip install poetry==2.3.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN if [ "$MODE" = "dev" ]; then \
        poetry install; \
    else \
        poetry install --only main; \
    fi

FROM python:3.13-slim AS runtime

RUN groupadd --system --gid 999 nonroot \
 && useradd --system --gid 999 --uid 999 --create-home nonroot

COPY --from=builder --chown=nonroot:nonroot /app /app
COPY --chown=nonroot:nonroot src /app/src

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONPATH=/app \
    PYTHONUNBUFFERED=1

USER nonroot

WORKDIR /app

CMD ["fastapi", "run", "--host", "0.0.0.0", "src/adapters/inbound/restapi/main.py"]
