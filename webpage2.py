# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:22:34 2012

@author: robert
"""

#from future import print_function
from flask import Flask, request
#from classes-demo import AddressBook, Person
import os

app = Flask("addresbook")
#book = AddressBook()
#if os.path.exists('addresses.xls')
#    book.load('addresses.xls')


@app.route('/')
def index():
    page = "This is my address book\n"
    #for person in book:
    #    page += "{1} {0}: {2}\n".format(person.first(), person.last(), person.phone())
    return page

app.run(debug=True)

#@app.route('/browse/<letter>')
#    def browse(letter):
#    (...)