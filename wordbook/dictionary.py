#!/usr/bin/env python3

import sys

from nltk.corpus import wordnet as wn

from exceptions import ApiException, DictionaryException


def list_definitions(word=None):
    if not word:
        word = input("Enter an English word:\n")
    definitions = None
    try:
        definitions = wn.synsets(word)
    except LookupError as lerror:
        raise DictionaryException(
            "Wordnet resource not found. Please download the nltk data"
        ) from lerror
    except Exception as ex:
        raise ApiException("An error ocurred while connecting with the API") from ex
    else:
        if not definitions:
            print(f"{word} is not an English word.")
        else:
            for i, definition in enumerate(definitions):
                print(f"{i + 1}. {definition.definition().capitalize()}.")


if __name__ == "__main__":
    if len(args := sys.argv[1:]) > 1:
        raise DictionaryException("Only one word is allowed.")
    list_definitions(args[0])
