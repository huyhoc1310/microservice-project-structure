help:
	@echo "  start         run server"
	@echo "  install       install dependencies"
	@echo "  lint          check style with flake8"
	@echo "  autopep8    auto format code pep8 with autopep8"
	@echo "  test          run all test suites"
	@echo "  coverage      export test coverage report"

start:
	ENV_FOR_DYNACONF=development python run.py

install:
	pip install -r requirements/dev.txt

lint:
	flake8 --exclude=migrations,venv --max-line-length=120 .

autopep8:
	autopep8 --in-place --recursive --exclude=migrations,venv --max-line-length=120 .

test:
	ENV_FOR_DYNACONF=testing python -m unittest -v

coverage:
	coverage run -m unittest
	coverage html

initdb:
	flask db init --directory src/db/migrations

migrate:
	flask db migrate --directory src/db/migrations
	flask db upgrade --directory src/db/migrations
