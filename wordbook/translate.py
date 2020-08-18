#!/usr/bin/env python3

import argparse
import os
import sys

# This is required for the tests to see the `util` package
if os.path.dirname(__file__) not in sys.path:
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from pathlib import Path
from googletrans import Translator

from exceptions import ApiException, TranslateException
from util.io import read_file, write_file

def translate(**kwargs):
    # Another way to do this is like:
    # source = 'en'
    # try:
    #     source = kwargs['source']
    # except KeyError:
    #     pass
    source = 'en' if 'source' not in kwargs else kwargs['source']
    dest = 'es' if 'dest' not in kwargs else kwargs['dest']
    file = None if 'file' not in kwargs else kwargs['file']
    text = None if 'text' not in kwargs else kwargs['text']
    if not text and not file:
        source = input('Enter the source language: ')
        dest = input('Enter the destination language: ')
        text = input('Enter a text to translate: ')
    elif file:
        if isinstance(file, str) and not Path(file).is_file():
            return 'Please provide a valid path to a file'
        if isinstance(file, str) and Path(file).suffix != '.txt':
            return 'Only .txt files are allowed'
        text = read_file(file)
    translated_text = ""
    try:
        translated_text = Translator().translate(text, dest=dest, source=source).text
    except ValueError as verror:
        raise TranslateException('The source or destination language is invalid.') from verror
    except Exception as ex:
        raise ApiException('An error ocurred while connecting with the API') from ex
    else:
        if file:
            output_file = 'data/output.txt' if 'output' not in kwargs else kwargs['output']
            write_file(translated_text, output_file)
        return translated_text

if __name__ == '__main__':
    my_parser = argparse.ArgumentParser(
        description='Translates a text or files'
    )
    my_parser.add_argument(
        'text',
        type=str,
        nargs='?',
        help='a text to be translated'
    )
    my_parser.add_argument(
        '--from',
        metavar='language',
        type=str,
        help='uses the supplied language as source'
    )
    my_parser.add_argument(
        '--to',
        metavar='language',
        type=str,
        help='uses the supplied language as destination'
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
    if args.text:
        kwargs['text'] = args.text
    if getattr(args, 'from'):
        kwargs['source'] = getattr(args, 'from')
    if args.to:
        kwargs['dest'] = args.to
    if args.file:
        kwargs['file'] = args.file
    print(translate(**kwargs))
