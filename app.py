#!/usr/bin/env python3

import argparse
import sys

from core.dictionary import list_definitions
from core.translate import translate

def parse_args():
    # Create the parser
    my_parser = argparse.ArgumentParser(
        description='Gets the definition of a word or translates a text or files'
    )
    # Add the arguments
    my_parser.add_argument(
        '-d',
        '--list-def',
        metavar='word',
        type=str,
        help='list the definitions of the given word'
    )
    my_parser.add_argument(
        '-t',
        '--translate',
        metavar='text',
        nargs='?',
        type=str,
        default=True,
        help='translates to Spanish the provided English text'
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
    return my_parser.parse_args()

if __name__ == "__main__":
    if not sys.argv[1:]:
        while True:
            text = input(
                '''Select the option you like to run:
                1) Find definitions
                2) Translate\n'''
            )
            if text == '1':
                list_definitions()
                break
            elif text == '2':
                print(translate())
                break
            else:
                print("Invalid option. Please try again.")
    args = parse_args()
    if args.list_def:
        list_definitions(args.list_def)
    elif args.translate:
        kwargs = {}
        if getattr(args, 'from'):
            kwargs['source'] = getattr(args, 'from')
        if args.to:
            kwargs['dest'] = args.to
        if args.file:
            kwargs['file'] = args.file
        print(translate(args.translate, **kwargs))
