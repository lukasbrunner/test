#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
(c) by Lukas Brunner under a MIT License (https://mit-license.org)

Authors:
- Lukas Brunner || l.brunner@univie.ac.at

Abstract:





"""

import numpy as np


def add_numbers(a, b):
    return np.sum([a, b])


def main():
    a =1
    b = 2
    c = add_numbers(a, b)
    print(c)
if __name__ == '__main__':
    main()
