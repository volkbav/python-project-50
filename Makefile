install:
	uv sync

lint:
	uv run ruff check brain_games

fix_lint:
	uv run ruff check --fix brain_games

.PHONY: install lint fix_lint