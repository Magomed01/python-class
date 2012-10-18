# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 20:04:27 2012

In-class example of classes.

@author: robert
"""

class Person(object):
    # constructor is __init__
    def __init__(self, first, last, number, city, state, zip, sex, height):
        self.firstname = first.title() # Capitalize first letter
        self.lastname = last
        self.phone = number
        self.city = city
        self.state = state
        self.zip = zip
        self.sex = sex
        self.heigh = height
    def fullname(self):
        return "{0} {1}".format(self.firstname, self.lastname)        
    def isLongDistance(self, areaCode):
        return self.phone[0:3] != str(areaCode)
    def setPhoneNumber(self, phone):
        self.phone = phone
    def setFirstName(self, firstname):
        self.firstname = firstname
    def setLastName(self, lastname):
        self.lastname = lastname
    def setSex(self, sex):
        self.sex = sex
    def setHeight(self, height):
        self.height = height        
        
t = Person("teague",
           "Jones",
           "415-867-5309",
           "SF",
           "CA",
           94122,
           "M",
           100)


# Access the firstname property
print t.firstname

# Call the fullname method
print t.fullname()       

# Do the same thing, again
print Person.fullname(t)

print t.isLongDistance('410')

t.setLastName('Jones')

print t.lastname, ' ', t.city, ', ', t.state

