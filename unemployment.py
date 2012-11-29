# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 18:34:40 2012

@author: robert
"""

import csv
from BeautifulSoup import BeautifulSoup

txt = """
Teague, Smith, Novato, 415-555-1234
John, Smith, San Rafael, 415-555-5678

"""

#lines = txt.split('\n')
#people = []
#for line in lines:
#  tokens = line.split(',')
#  people.append({
#    'first': tokens[0],
#    'last': tokens[1],
#    'city': tokens[2],
#    'phone': tokens[3],    
#  })
  
# Split each line by commas after getting lines by splitting on newline
#[Person(*l.split(',')) for l in txt.split('\n')]
# Equiv.: [Person(*['Teague', 'Smith', 'Novato', '415-555-1234']) ... ]
# which resolves to: [Person('Teague', 'Smith', 'Novato', ...) ... ]

# Open a CSV file and parse it
levels = {}
with open('unemployment09.csv', 'r') as f:
  reader = csv.reader(f, delimiter=',')
  for row in reader:
    try:    
      id = ''.join(row[1:3])
      rate = float(row[-1].strip()) # get the last column as a float
      levels[id] = rate
    except:
      print "error!"
    #print rate
  
  lowest = min(levels.values())
  highest = max(levels.values())
  spread = highest - lowest
  deltas = { k: ((v - lowest)/spread)*255 for k,v in levels.items() }

  
# Open an SVG file and color-code counties with unemployment rates
with open('counties.svg', 'r') as svg:
    # Treat weird 'sodipodi' tags as self-closing
    soup = BeautifulSoup(svg.read(), selfClosingTags=['defs', 'sodipodi: namedview'])
counties = soup.findAll('path')

# We'll replace the style tags in the SVG text
# but it would be beter to do a dictionary of key/value pairs here...
STYLE = "font-size:12px;fill-rule:nonzero;stroke:#000000;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:"

for county in counties:
  county_id = county['id']
  if county_id in ('separator', 'State_lines'):
    continue
  if county_id in deltas:
    delta = deltas[county_id]
    sub = int(255 - delta) # we're putting together a hex color like #FF0000
    color = ("%0.2x"*3).format(255, sub, sub) # repeat hex value three times
    county['style'] = STYLE + color
    print color

with open('new-counties-unemp.svg', 'w') as f:
  f.write(soup.prettify)




