install:
	poetry install

reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

test:
	poetry run pytest

# test-coverage:
# 	poetry run pytest --cov=test --cov-report xml

lint:
	poetry run flake8 test

selfcheck:
	poetry check

build:
	poetry build

update Playwright:
	pip install pytest-playwright playwright -U

.PHONY: install test lint selfcheck check build
