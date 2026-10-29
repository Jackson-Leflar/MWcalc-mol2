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
def main():
    filename = sys.argv[1]
    with open(filename, 'r') as mol2File:
        in_molecule = False
        mols = []
        mol_lines = []
        mol_file_lines = mol2File.readlines()
        for line in mol_file_lines:
            if "@<TRIPOS>MOLECULE" in line:
                in_molecule = True                    
                continue
            if "ROOT" in line:
                in_molecule = False
                mol_lines.append(line)
                mols.append(mol_lines)                    
                mol_lines = []
                continue
    
            if in_molecule == True:
                mol_lines.append(line)

        in_atoms = False
        atoms = [] 
        mw_counter = 0
        for mol in mols:
            for line in mol:
                if "@<TRIPOS>ATOM" in line:
                    in_atoms = True
                    continue
                if "@<TRIPOS>BOND" in line:
                    in_atoms = False
                    for atom in atoms:
                        mw_counter += ATOMIC_WEIGHTS[atom]
                    
                if in_atoms == True:
                    line_split = line.split()
                    element = line_split[5].split(".")[0]
                    atoms.append(element)            
    
            print(f"{mw_counter:.3f}")
            mw_counter = 0
            atoms = []
            continue


if __name__ == "__main__":
    main()
