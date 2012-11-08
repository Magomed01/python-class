# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 19:58:25 2012

@author: robert
"""

from collections import Counter

def print_menu():
  print "Enter a value, or X to exit."

value = ""
values = list()
cnt = Counter()
while (value != "X"):
  print_menu()
  value = raw_input("> ")
  if (value != "X"):
    values.append(float(value))

print "\n"

# Print mean
sum = 0
for v in values:
  sum += v
print "Mean:", sum / len(values)

# Print median
values.sort()
if (len(values) % 2 == 0):
  val1 = values[len(values) / 2 - 1]
  val2 = values[len(values) / 2]
  print "Median:", (val1 + val2) / 2.0 
else:
  print "Median:", values[len(values) / 2]

# Print mode
cnt = Counter(values)
mode = cnt.most_common(1)[0]
print "Mode:", mode[0]

