.PHONY: install

install:
	pipenv install
	python -m nltk.downloader wordnet
