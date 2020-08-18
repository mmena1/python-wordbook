.PHONY: install test run lint

install:
	# --pre is required for black
	pipenv install --pre
	pipenv run python -m nltk.downloader wordnet

test:
	pipenv run python -m unittest

run:
	pipenv run python wordbook/runner.py

lint:
	pipenv run black .
	pipenv run flake8