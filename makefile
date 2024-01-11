.PHONY: venv-create install

## ENV SETUP
venv-create:
	python -m venv venv

install:
	pip install -r requirements.txt


## DEVELOPMENT helpers
lint:
	black .
	ruff check --fix . --ignore E501
	djlint . --reformat
	isort . --profile black

celery:
	celery -A imagegenerator worker --beat -l INFO

redis:
	docker run -p 15158:15158 redis
