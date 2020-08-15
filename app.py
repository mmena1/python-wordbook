#!/usr/bin/env python3

import nltk
import sys

from nltk.corpus import wordnet as wn

def main(word):
    definitions = wn.synsets(word)
    if not definitions:
        print(f"{word} is not an English word.")
    for definition in definitions:
        index = definitions.index(definition)
        print(f"{index + 1}. {definition.definition().capitalize()}.")

if __name__ == "__main__":
    user_input = sys.argv[1:]
    if len(user_input) > 1:
        print("Only one word is allowed.")
    elif not user_input:
        text = input("Enter an English word:\n")
        main(text)
    else:
        main(sys.argv[1])
