install:
	uv sync

lint:
	uv run ruff check .

fix_lint:
	uv run ruff check --fix .

build:
	uv build

package-install:
	uv tool install --force dist/*.whl

upgrade: build package-install

help:
	uv run gendiff --help

run:
	uv run gendiff ./tests/test_data/file1.json ./tests/test_data/file2.json

test:
	uv run pytest -svv

.PHONY: install lint fix_lint build package-install upgrade help run test