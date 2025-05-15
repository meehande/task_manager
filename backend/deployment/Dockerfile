FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/


COPY ./ app/

WORKDIR /app/

RUN uv sync --frozen --no-dev


EXPOSE 8000

CMD ["uv", "run", "python", "-m", "task_manager.main"]

