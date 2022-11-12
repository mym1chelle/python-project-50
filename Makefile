install:
	poetry install

run-gendiff:
	poetry run gendiff

gendiff-h:
	poetry run gendiff -h

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

lint:
	poetry run flake8 gendiff

test-gendiff:
	poetry run pytest -s

test-cov-gendiff:
	poetry run pytest --cov=gendiff --cov-report xml