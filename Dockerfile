FROM python:3.12.13-slim

WORKDIR app

RUN  apt update \
     && apt install curl -y \
     && curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH=/root/.local/bin:$PATH
ENV UV_PROJECT_ENVIRONMENT=/usr/local/

COPY pyproject.toml .
COPY uv.lock .
RUN uv sync --frozen

COPY ./app .

CMD uv run alembic upgrade head && uv run fastapi run main.py
