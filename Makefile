start:
	uv run src/main.py

lint:
	uv run ruff check .

.PHONY: start
