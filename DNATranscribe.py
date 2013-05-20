"""
Rosalind: Transcribing DNA into RNA
Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.
Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
Sample Dataset
GATGGAACTTGACTACGTAAATT Sample Output
GAUGGAACUUGACUACGUAAAUU

"""

f = open('rosalind_rna.txt')
s = f.read().strip()
tras = {'T':'U'}
new_s = [tras[c] if c == 'T' for c in s]
print ().join(new_s)