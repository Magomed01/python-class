#/usr/bin/env python

import os
import csv
import sys

from BeautifulSoup import BeautifulSoup

UNKNOWN_COLOR = (128, 128, 128)  # Some type of Grey

COLOR_TEMPLATE_OLD = "#%0.2X%0.2X%0.2X"     # Hex color using " % " style
COLOR_TEMPLATE_NEW = "#{:02X}{:02X}{:02X}"  # Hex color using .format()

# We can split lines up like this if we really want
STYLE_TEMPLATE = "font-size:12px;fill-rule:nonzero;stroke:#000000;"\
                 "stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;"\
                 "stroke-dasharray:none;stroke-linecap:butt;"\
                 "marker-start:none;stroke-linejoin:bevel;fill:{fill}"

source_file = sys.argv[1] if len(sys.argv) > 1 else "unemployment09.csv"

if len(sys.argv) > 2:
    output_file = sys.argv[2]
else:
    folder = os.path.dirname(source_file)
    source_name = os.path.basename(source_file)
    base, ext = os.path.splitext(source_name)
    output_file = os.path.join(folder, "{0}.svg".format(base))

rates = {}
with open(source_file, 'r') as data:
    reader = csv.reader(data, delimiter=",")
    for row in reader:
        try:
            county_id = row[1].strip() + row[2].strip()
            rate = float(row[-1].strip())
            rates[county_id] = rate
        except:
            print "Error in {}".format(row)

lowest = min(rates.values())
highest = max(rates.values())
spread = highest - lowest
# Let's create a little helper function for ourselves

# Make the delta for each county a value between 0 and 255 with
# the highest unemployment being 0 and the lowest being 255
# We use this to create a color that is "less white" and
# "more red" based on unemployment rates.
calc_delta = lambda rate: 255 - int(round(255 * (rate - lowest) / spread))
deltas = {k: calc_delta(v) for (k, v) in rates.items()}

with open('counties.svg', 'r') as svg:
    soup = BeautifulSoup(svg.read(),
                         selfClosingTags=['defs', 'sodipodi:namedview'])
paths = soup.findAll('path')
counties = (p for p in paths if p['id'] not in ["State_Lines", "separator"])

for county in counties:
    county_id = county['id']
    if county_id in rates:
        delta = deltas[county_id]
        color = (255, delta, delta)
    else:
        color = UNKNOWN_COLOR

    color_code = COLOR_TEMPLATE_OLD % color  # Using old style "%" operator
    color_code = COLOR_TEMPLATE_NEW.format(*color)  # Using .format()
    county['style'] = STYLE_TEMPLATE.format(fill=color_code)

with open(output_file, 'w') as svg:
    svg.write(soup.prettify())
