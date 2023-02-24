export PYTHONPATH=src

console:
	@poetry run flask shell

start:
	flask --app app --debug run --port 8080
	#poetry run flask run -h 0.0.0.0 -p 8080

test:
	poetry run pytest -vv tests/test_post_delete.py
