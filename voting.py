# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 19:17:35 2012

@author: robert
"""

def print_menu():
  print "##################################################"
  print "# WELCOME TO THE WORLD'S CHEAPEST VOTING MACHINE #"
  print "##################################################"
  print "\n"
  print "Choose a candidate, or type X to exit" 
  print "\n"
  print "1. Eisenhower"
  print "2. Patton"
  print "3. MacArthur"

vote = ""
d = {'eisenhower':0, 'patton':0, 'macarthur':0}
while (vote != "X"):
  print_menu()  
  vote = raw_input("> ")
  if (vote == "1"): d['eisenhower'] = d['eisenhower'] + 1
  if (vote == "2"): d['patton'] = d['patton'] + 1
  if (vote == "3"): d['macarthur'] = d['macarthur'] + 1
  if (vote != "X"):
    print "Thank you for voting"
print "Tally: ", d  


