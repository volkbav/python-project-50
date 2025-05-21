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
	uv run gendiff ./tests/test_data/big_file1.json ./tests/test_data/big_file2.json
	uv run gendiff ./tests/test_data/big_file1.yml ./tests/test_data/big_file2.yml

test:
	uv run pytest -svv

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml

.PHONY: install lint fix_lint build package-install upgrade help run test test-coverage