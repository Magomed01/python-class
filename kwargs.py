#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 20:44:55 2012

@author: robert
"""

def funct(arg1, arg2, arg3, *args, **kwargs):
    print "1=", arg1
    print "2=", arg2
    print "3=", arg3
    print "args=", args
    print kwargs

def lots_of_parms(**kwargs):
    return "string {name} {address}".format(**kwargs)

    
args = [1, 2, 3, 4, 5, 6]

# Splat arguments
funct(*args)

# Specifying args by their parameter name in the function
funct(arg2="abc", arg1="hello", arg3="yes", body="YES")

# Keyword arguments
kwargs = {'arg1': 1,
          'arg2': "two",
          'arg3': "THREE",
          'class': "done"}
funct(**kwargs)

print lots_of_parms(name="so and so", address="123")
