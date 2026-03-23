install:
	uv sync

test:
	uv run pytest

test-coverage:
	uv run pytest --cov

lint:
	uv run ruff check