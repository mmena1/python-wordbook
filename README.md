# Python thesaurus app
This app uses [wordnet](https://www.nltk.org/howto/wordnet.html) in order to find definitions to English words provided by the user. Similar to [this](http://wordnetweb.princeton.edu/perl/webwn).

## Why?
Nothing in particular, playing a bit with Python as part of my self-training.

## Requirements
- Python 3.8
- [Pipenv](https://pypi.org/project/pipenv/)

## Instructions
1. Install the dependencies and the [wordnet data](https://www.nltk.org/data.html):

    ```bash
    make install
    ```

1. Execute the script with an English word as an argument:

    ```bash
    pipenv run python app.py dog
    ```
    Or:
    ```bash
    pipenv run python app.py
    ```
    You will be prompted to enter a word.
