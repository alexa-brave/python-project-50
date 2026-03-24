install:
	uv sync

test:
	uv run pytest

test-coverage:
	uv run pytest --cov --cov-report=xml:tests/coverage/coverage.xml
lint:
	uv run ruff check