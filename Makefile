export PYTHONPATH=src

console:
	@poetry run flask shell

start:
	flask --app app --debug run

test:
	poetry run pytest -vv tests
