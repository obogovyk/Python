#!/usr/bin/python
# -*- coding: utf-8 -*-
# pgutil v.1.0.14

'''
Copyright(C) 2015 Bogovyk Oleksandr <obogovyk@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

import random, string
import argparse
import os

parser = argparse.ArgumentParser(description='Help for pgutil.')
parser.add_argument('-c', '--count', type=int, default=6, help="Password count number.")
parser.add_argument('-l', '--lenght', type=int, default=8, help="Password lenght number.")
parser.add_argument('-n', '--numbers', type=str, default=False, help="Use numbers.")
parser.add_argument('-s', '--symbols', type=str, default=False, help="Use special symbols like '!@#$&*()'.")

class pgutil:

    numbers = ""
    symbols = ""

    pg_string = ""

    def __init__(self, count, lenght, is_numbers, is_symbols, is_unique):
        self.count = count
        self.lenght = lenght
        self.is_numbers = is_numbers
        self.is_symbols = is_symbols
        self.is_unique = is_unique

    def pg_generate(self):

        if(self.is_numbers == "True"):
            self.numbers = string.digits
        else:
            self.numbers = str("")

        if(self.is_symbols == "True"):
            self.symbols = "!@#$%^&*()"
        else:
            self.symbols = str("")

        self.pg_string = self.numbers + string.ascii_letters + self.symbols

        for x in range(0,self.count):
            random.seed = (os.urandom(2048))
            print ''.join(random.choice(self.pg_string) for i in range(self.lenght))

pg = pgutil(parser.parse_args().count,
            parser.parse_args().lenght,
            parser.parse_args().numbers,
            parser.parse_args().symbols,
            parser.parse_args().unique)

pg.pg_generate()
