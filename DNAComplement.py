"""
Rosalind: Complementing a Strand of DNA

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s.
Sample Dataset
AAAACCCGGT Sample Output
ACCGGGTTTT
"""

f = open('rosalind_revc.txt')

s = f.read().strip()

s = s[::-1]

tras = {'A':'T', 'T':'A', 'C':'G', 'G':'T'}

new_s = [tras[c] for c in s]

print ('').join(new_s)