#!/usr/bin/env python3

import argparse
import sys

from core.thesaurus import list_definitions

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
    args = parse_args()
    if args.list_def:
        list_definitions(args.list_def)
