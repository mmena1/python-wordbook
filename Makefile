.PHONY: install test run

install:
	pipenv install
	python -m nltk.downloader wordnet

test:
	pipenv run python -m unittest

run:
	pipenv run python wordbook/runner.py