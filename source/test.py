#! /usr/bin/env python

import os, sys

x = os.getcwd()
print(x)

if os.path.relpath('/home/arpit/repositories/Mathjax/Mathjax.js?config=default.js',x):
    print('true')
else:
    print('false')
