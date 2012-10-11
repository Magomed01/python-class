# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 20:04:27 2012

In-class example of classes.

@author: robert
"""

class Person(object):
    # constructor is __init__
    def __init__(self, first, last, number):
        self.firstname = first.title() # Capitalize first letter
        self.lastname = last
        self.phone = number
    def fullname(self):
        return "{0} {1}".format(self.firstname, self.lastname)        
    def isLongDistance(self, areaCode):
        return self.phone[0:3] != str(areaCode)

        
t = Person("teague",
           "Jones",
           "415-867-5309")


# Access the firstname property
print t.firstname

# Call the fullname method
print t.fullname()       

# Do the same thing, again
print Person.fullname(t)

print t.isLongDistance('410')

# TODO Add city, state, zip, plus two more(your choice), setPhoneNumber,
# setFirstName, setLastName

