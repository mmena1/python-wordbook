#!/usr/bin/env python3

import argparse
import sys

from pathlib import Path
from googletrans import Translator
from util.io import read_file, write_file

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
    file = None if 'file' not in kwargs else kwargs['file']
    if not args and not file:
        source = input('Enter the source language: ')
        dest = input('Enter the destination language: ')
        text = input('Enter a text to translate: ')
    elif args and isinstance(args[0], list):
        text = ' '.join(args[0])
    elif args and isinstance(args[0], str):
        text = (args[0])
    else:
        if isinstance(file, str) and not Path(file).is_file():
            return 'Please provide a valid path to a file'
        if isinstance(file, str) and Path(file).suffix != '.txt':
            return 'Only .txt files are allowed'
        text = read_file(file)
    translated_text = Translator().translate(text, dest=dest, source=source).text
    if file:
        output_file = 'output/translated.txt' if 'output' not in kwargs else kwargs['output']
        write_file(translated_text, output_file)
    return translated_text

if __name__ == '__main__':
    my_parser = argparse.ArgumentParser(
        description='Translates a text or files'
    )
    my_parser.add_argument(
        '-f',
        '--file',
        metavar='path_to_file',
        type=str,
        help='translates the provided file'
    )
    args = my_parser.parse_args()
    kwargs = {}
    if args.file:
        kwargs['file'] = args.file
        print(translate(**kwargs))
    else:
         print(translate(sys.argv[1:]))
