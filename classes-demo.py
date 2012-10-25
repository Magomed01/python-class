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
        if phone.isdigit() and len(phone) in [7,10]:
          self.phone = phone
        else:
          raise ValueError("Phone number must be a 7 or 10-digit string.")
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
            self.people = []
        else:
            self.people = people
    def first(self):
        return self.first
    def last(self):
        return self.last
    def phone(self):
        return self.phone
    def addPerson(self, person):
        self.people.append(person)
    def findByLastName(self, lastname):
        found = AddressBook()
        for person in self.people:
            if lastname == person.last:
                found.addPerson(person)
        return found
    def getPeople(self):
        people = []
        # .extend() is like append, but appends a list
        people.extend(self.people)
        return people # or just do self.people[:]
    def firstBeginsWith(self, prefix):
        found = [] # initialize our list
        for person in self.people:
            if person.first().lower().startswith(prefix.lower()):
                found.append(person)
        """
 Note: Could do this whole method in a single line as a list comprehension:
 return AddressBook([person for person in self.people if \
                     person.first().lower().startswith(person.lower())])
        """
        # return a *new* address book here
        return AddressBook(found) 
    def getByName(self, first, last):
        found = AddressBook()
        for person in self.person:        
            if person.first() == first and person.last() == last:
                found.add(person)
        return found
#    # print to CSV
#    def export(self, path):
#        with open(path, mode="w") as f: # f is a filehandle
#            for person in self.people:
#                #print("\t".join([person.first(), person.last(), person.phone()]), file=f)
#                print "entry" #syntax above is wrong
#        
#    def import(self, path):
#        self.add(Person(*line.split())) # clever! dump all arguments as a splat arg
#        open(path, mode="r") as f:
#            for line in f:
#                self.add(Person(#line.split()))
                

try:
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
  t.setPhoneNumber("555---1212")
  print t.isLongDistance("408")
  t.setPhoneNumber("3135551212")
  print t.isLongDistance("408")
  print t.isLongDistance("313")
except ValueError as e:
  print("Error: " + str(e))

book = AddressBook()
book.addPerson("Wright")
