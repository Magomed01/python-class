# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 19:37:45 2012

In-class example for named tuples.

@author: robert
"""

from collections import namedtuple

# atom = ( 'C", 1, 2, 17, 'HIS')

# Define the structure for the Atom namedtuple
Atom = namedtuple("Atom", "element x y z residue")

# Create an instance of Atom
atom2 = Atom('C', 1, 2, 17, 'HIS')

# Now can use accessors like atom2.element, atom2.x, atom2.residue
print atom2.element



Monkey = namedtuple("Monkey", "headColor age name")
myMonkey = Monkey("red", 12, "Joe")
print myMonkey.name


