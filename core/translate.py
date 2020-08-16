#!/usr/bin/env python3

import sys

from googletrans import Translator

def translate(*args, **kwargs):
    text = ''
    # Another way to do this is like:
    # source = 'en'
    # try:
    #     source = kwargs['source']
    # except KeyError:
    #     pass
    source = 'en' if 'source' not in kwargs else kwargs['source']
    dest = 'es' if 'dest' not in kwargs else kwargs['dest']
    if not args:
        source = input('Enter the source language: ')
        dest = input('Enter the destination language: ')
        text = input('Enter a text to translate: ')
    else:
        if isinstance(args[0], list):
            text = ' '.join(args[0])
        else:
            text = (args[0])
    translator = Translator()
    print(translator.translate(text, dest=dest, source=source).text)

if __name__ == '__main__':
    translate(sys.argv[1:])
