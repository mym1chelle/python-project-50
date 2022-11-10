install:
	poetry install

gendiff-h:
	poetry run gendiff -h

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff