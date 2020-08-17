#!/usr/bin/env python3

import nltk
import sys

from nltk.corpus import wordnet as wn

def list_definitions(word=None):
    if not word:
        word = input('Enter an English word:\n')
    definitions = wn.synsets(word)
    if not definitions:
        print(f'{word} is not an English word.')
    for i, definition in enumerate(definitions):
        print(f'{i + 1}. {definition.definition().capitalize()}.')

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) > 1:
        print('Only one word is allowed.')
        sys.exit(2)
    list_definitions(args[0])
