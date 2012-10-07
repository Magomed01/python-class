#!/usr/bin python
# Robert Theis
# Sept. 15, 2012
# Introduction to Python Programming

# Parses a valid Protein Data Bank (PDB) format text file for a protein.

import argparse, os, requests, sys

def atom_element(atom):
    return atom[0]

def atom_residue(atom):
    return atom[1]

def atom_x_pos(atom):
    return atom[2]

def atom_y_pos(atom):
    return atom[3]

def atom_z_pos(atom):
    return atom[4]

def bounding_box(x_range, y_range, z_range):
    return [(x_range[0], y_range[0], z_range[0]), \
            (x_range[0], y_range[0], z_range[1]), \
            (x_range[0], y_range[1], z_range[0]), \
            (x_range[0], y_range[1], z_range[1]), \
            (x_range[1], y_range[0], z_range[0]), \
            (x_range[1], y_range[0], z_range[1]), \
            (x_range[1], y_range[1], z_range[0]), \
            (x_range[1], y_range[1], z_range[1])]

def build_url(id):
    return "http://www.rcsb.org/pdb/download/downloadFile.do?fileFormat=pdb" + \
           "&compression=NO&structureId={0}".format(id)

def download_pdb(pdbid):
    # Download the file
    print "Downloading..."
    r = requests.get(build_url(pdbid))
    if r.status_code != 200:
        sys.exit("Downoad failed.")
    print "Download complete."
    return r.text

def is_atom_line(line):
    if line[:4] == 'ATOM':
        return True
    else:
        return False

def is_header_line(line):
    if line[:6] == 'HEADER':
        return True
    else:
        return False

def is_title_line(line):
    if line[:5] == 'TITLE':
        return True
    else:
        return False

def openfile(filename):
    fh = open(filename, "r+")
    str = fh.read()
    fh.close()
    return str

# Returns a data structure representing an atom: element, residue, and position
def parse_atom_line(line):
    if is_atom_line(line) == False:
        return False
    # element, residue, x-position, y-position, z-position
    return list([line[76:78], line[17:20], line[30:38], line[38:46], line[46:54]])

# Goes through all PDB lines and tallies properties for the protein as a whole
# Returns a PDB dictionary representing the tallied values for the protein
def parse_pdb(pdb_lines):
    pdb = {'id': None, 'title': '', 'atom_count': 0, 'corners': None, 'volume': 0}
    residues = {}
    atom_count = 0
    x_range = (None, None)
    y_range = (None, None)
    z_range = (None, None)
    for line in pdb_lines:
        if is_atom_line(line) == True:
            # Increase atom count            
            atom_count = atom_count + 1
            
            # Check position values            
            atom = parse_atom_line(line)
            x_range = update_range(x_range, atom_x_pos(atom))
            y_range = update_range(y_range, atom_y_pos(atom))
            z_range = update_range(z_range, atom_z_pos(atom))
            
            # Tally the residue            
            residue = line[17:20]
            if residue in residues:
                residues[residue] = residues[residue] + 1
            else:
                residues[residue] = 1
        elif is_title_line(line):
            pdb['title'] = pdb['title'].rstrip() + line[10:] + ' '
        elif is_header_line(line):
            pdb['id'] = line[62:66]
    pdb['atom_count'] = atom_count
    pdb['corners'] = bounding_box(x_range, y_range, z_range)
    pdb['volume'] = volume(x_range, y_range, z_range)
    return pdb

# Returns the atom count for a protein, given a PDB dictionary
def pdb_atom_count(pdb):
    return pdb['atom_count']

# Returns the corners of the 3D bounding box for a protein, given a PDB dictionary
def pdb_bounding_box_corners(pdb):
    return pdb['corners']

# Returns the volume of the 3D bounding box for a protein, given a PDB dictionary
def pdb_bounding_box_volume(pdb):
    return pdb['volume']

# Returns the PDB ID, given a PDB dictionary
def pdb_id(pdb):
    return pdb['id']

def pdb_lines(pdb_data):
    return pdb_data.split('\n')

def pdb_title(pdb):
    return pdb['title']

# Given a minimum/maximum value pair and a number, returns an updated min/max if
# the number falls outside of the min/max range, otherwise returns original pair
def update_range(old_range, num):
    num = float(num)    
    if old_range[0] == None: # range is undefined for the first run
        return(num, num)
    min = old_range[0]
    max = old_range[1]
    if num < min:
        min = num
    elif num > max:
        max = num
    return (min, max)

def validate_pdbid(pdbid):
    if len(pdbid) != 4:
        return False
    for char in pdbid:
        if char.isalpha() == False and char.isdigit() == False:
            return False
    return True
    
def volume(x_range, y_range, z_range):
    x = float(x_range[1]) - float(x_range[0])
    y = float(y_range[1]) - float(y_range[0])
    z = float(z_range[1]) - float(z_range[0])
    return x * y * z

def main():
  parser = argparse.ArgumentParser(add_help=True)
  parser.add_argument('id', action="store")
  opts = parser.parse_args()
  filename= opts.id + '.pdb'
  if not os.path.exists(filename):
    fh = open(filename, "w")
    fh.write(download_pdb(opts.id))
    fh.close()
  pdbfile = openfile(filename)
  pdb = parse_pdb(pdb_lines(pdbfile))
  print "TITLE: ", pdb_title(pdb)
  print "ID: ", pdb_id(pdb)
  print "ATOM COUNT: ", pdb_atom_count(pdb)
  print "CORNERS: ", pdb_bounding_box_corners(pdb)
  print "VOLUME: ", pdb_bounding_box_volume(pdb)

main()
