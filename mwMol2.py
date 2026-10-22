#!/usr/bin/env python3
"""
mwMol2.py
Read in a mol2 file and calculate every molecule's molecular weight
Jackson Leflar
Date Last edited: October 22, 2026
Usage: python3 mwMol2.py <.mol2 file>
"""
import re
import sys
# Step 1: create dictionary of atomic weights
ATOMIC_WEIGHTS = {"H": 1.008, "C": 12.011, "N": 14.007, "O": 15.999, "F": 18.998 , "Na": 22.990,\
                   "P": 30.974, "S": 32.066, "Cl": 35.453, "Br": 79.904, "Ca": 40.078}
# Step 2: read in mol2 file
with open(sys.argv[1], 'r') as mol2File:
    content = mol2File.read()
    print(content)





# Step 3: start reading each molecule at "@<TRIPOS>ATOM" and end at "0 ROOT"