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
	uv run gendiff ./gendiff/files/file1.json ./gendiff/files/file2.json

test:
	uv run pytest -s

.PHONY: install lint fix_lint build package-install upgrade help run test