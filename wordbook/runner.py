#!/usr/bin/env python3

import argparse
import sys

from dictionary import list_definitions
from translate import translate

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
