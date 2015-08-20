#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
PGUtil v0.1.21
Simple, but strong password generator utility.

This program comes with ABSOLUTELY NO WARRANTY; for details type `pgutil --help'.
This is free software, and you are welcome to redistribute it
under certain conditions.

Copyright(C) 2015 Bogovyk Oleksandr <obogovyk@gmail.com>
'''

import random, string
import argparse
import sys
import os

parser = argparse.ArgumentParser(description='Help for PGUtil v0.1.21')
parser.add_argument('-c', '--count', type=int, default=5, choices=range(1,100), help="Password count number (5 is default)")
parser.add_argument('-l', '--lenght', type=int, default=8, choices=range(6,16), help="Password lenght number (8 is default)")
parser.add_argument('-n', '--numbers', action='store_true', default=False, help="Use numbers in password.")
parser.add_argument('-s', '--symbols', action='store_true', default=False, help="Use special symbols in password like !()@#$&.,?{}*.")

class pgutil:

    pg_string = ""
    pg_list = []

    def __init__(self, count, lenght, is_numbers, is_symbols):
        self.count = count
        self.lenght = lenght
        self.is_numbers = is_numbers
        self.is_symbols = is_symbols

    def pg_generate(self):

        if(self.is_numbers is True):
            self.numbers = string.digits
        else:
            self.numbers = str("")

        if(self.is_symbols is True):
            self.symbols = "`~!@#$%^&*()-_=+[]{};:,<.>?"
        else:
            self.symbols = str("")

        self.pg_string = string.ascii_letters + self.numbers + self.symbols

        for x in range(0,self.count):
            self.pg_list.append(''.join(random.choice(self.pg_string) for i in range(self.lenght)))
            
        for password in self.pg_list:
            print(password)
        
if __name__ == "__main__":
    pg = pgutil(parser.parse_args().count,
    parser.parse_args().lenght,
    parser.parse_args().numbers,
    parser.parse_args().symbols)

    pg.pg_generate()
