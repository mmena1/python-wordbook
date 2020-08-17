#!/usr/bin/env python3

import nltk
import sys

from nltk.corpus import wordnet as wn

def list_definitions(*args):
    word = ''
    if len(args) > 1:
        print('Only one word is allowed.')
        sys.exit(2)
    elif not args:
        word = input('Enter an English word:\n')
    else:
        word = args[0]
    definitions = wn.synsets(word)
    if not definitions:
        print(f'{word} is not an English word.')
    for i, definition in enumerate(definitions):
        print(f'{i + 1}. {definition.definition().capitalize()}.')

if __name__ == '__main__':
    list_definitions(sys.argv[1:])
