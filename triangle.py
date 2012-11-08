# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 18:49:53 2012

@author: robert
"""
import argparse

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('a', action="store")
parser.add_argument('b', action="store")
opts = parser.parse_args()

float_a = float(opts.a)
float_b = float(opts.b)
print "The length of the third side is", (float_a**2 + float_b**2)**0.5, "!"
