#!/usr/bin/env python3
"""
mwMol2.py
Read in a mol2 file and calculate every molecule's molecular weight
Jackson Leflar
Date Last edited: October 26, 2026
Usage: python3 mwMol2.py <.mol2 file>
"""
import re
import sys
# Step 1: create dictionary of atomic weights
ATOMIC_WEIGHTS = {"H": 1.008, "C": 12.011, "N": 14.007, "O": 15.999, "F": 18.998 , "Na": 22.990,\
                   "P": 30.974, "S": 32.066, "Cl": 35.453, "Br": 79.904, "Ca": 40.078}
# Step 2: read in mol2 file and look for every element
def ReadMolecules(filename):
    molecules = []
    with open(filename, 'r') as mol2File:
        for line in mol2File:
            #for element in re.search(r"([A-Z][a-z]?)", mol2File):
            #    print(element.group())
            #    molecules.append((element.group()))
            line_split = line.split()
            if len(line_split) >= 6:
                if line_split[5] == "****":
                    break
                molecules.append((line_split[5]))
    
    return molecules

def molecular_weight(filename):
    total = 0.0
    for element in ReadMolecules(filename):
        if element in ATOMIC_WEIGHTS:
            total += ATOMIC_WEIGHTS[element]
        elif element not in ATOMIC_WEIGHTS:
            total += ATOMIC_WEIGHTS[element[0]]
        else: 
            raise ValueError(f"Unknown Element {element}")
    return total

# Step 3: start reading each molecule at "@<TRIPOS>ATOM" and end at "0 ROOT"
# def splitmolecules


def main():
    print(ReadMolecules(sys.argv[1]))
    print(molecular_weight(sys.argv[1]))


if __name__ == "__main__":
    main()
