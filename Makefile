install:
	uv sync

lint:
	uv run ruff check brain_games

fix_lint:
	uv run ruff check --fix brain_games

build:
	uv build

package-install:
	uv tool install --force dist/*.whl

upgrade: build package-install

.PHONY: install lint fix_lint build package-install upgrade