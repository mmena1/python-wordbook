.PHONY: install test

install:
	pipenv install
	python -m nltk.downloader wordnet

test:
	pipenv run python -m unittest