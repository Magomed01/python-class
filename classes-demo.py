# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 20:04:27 2012

In-class example of classes.

@author: robert
"""

class Person(object):
    # constructor is __init__
    def __init__(self, first, last, number, city, state, zipcode, sex, height):
        self.firstname = first.title() # Capitalize first letter
        self.lastname = last
        self.phone = number
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.sex = sex
        self.height = height
    def fullname(self):
        return "{0} {1}".format(self.firstname, self.lastname)        
    def isLongDistance(self, areaCode):
        if len(self.phone) < 9:
            return False
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

class AddressBook(object):
    def __init__(self, people=None):
        if people is None:
            people = "None"
        self.people = people
    def addPerson(self, person):
        self.people.append(person)
    def findByLastNam(self, lastname):
        found = AddressBook()
        for person in self.people:
            if lastname == person.last:
                found.addPerson(person)
        return found
        

t = Person("teague",
           "Smith",
           "415-867-5309",
           "SF",
           "CA",
           94122,
           "M",
           100)


# Access the firstname property
print t.firstname

# Call the fullname method
print t.fullname() # Fullname is a fuction, do don't forget the parentheses  

# Do the same thing, again
print Person.fullname(t)

print t.isLongDistance('410')

t.setLastName('Jones')

print t.lastname, ' ', t.city, ', ', t.state
t.setPhoneNumber("555-1212")
print t.isLongDistance("408")
t.setPhoneNumber("313-555-1212")
print t.isLongDistance("408")
print t.isLongDistance("313")

book = AddressBook()
book.addPerson("Wright")
