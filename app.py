#!/usr/bin/env python3

import argparse
import sys

from core.thesaurus import list_definitions
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
        help='translates to Spanish the provided English text'
    )
    my_parser.add_argument(
        '--from',
        metavar='language',
        type=str,
        help='uses the suplied language as source'
    )
    my_parser.add_argument(
        '--to',
        metavar='language',
        type=str,
        help='uses the suplied language as destination'
    )
    return my_parser.parse_args()

if __name__ == "__main__":
    if not sys.argv[1:]:
        text = input(
            '''Select the option number you like to do:
            1) Find definitions
            2) Translate\n'''
        )
        if text == '1':
            list_definitions()
        elif text == '2':
            translate()
        else:
            print("Invalid option.")
            sys.exit(2)
    args = parse_args()
    if args.list_def:
        list_definitions(args.list_def)
    elif args.translate:
        kwargs = {}
        if getattr(args, 'from'):
            kwargs['source'] = getattr(args, 'from')
        if args.to:
            kwargs['dest'] = args.to
        translate(args.translate, **kwargs)
