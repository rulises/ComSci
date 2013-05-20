"""
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
Sample Dataset
GAGCCTACTAACGGGAT CATCGTAATGACGGCCT
Sample Output
7
"""

f = open('rosalind_hamm.txt')
s = list(f.next().strip())
t = list(f.next().strip())

comp = zip(s,t)
ss = 0
for (x, y) in comp:
	if x != y:
		ss+=1
print ss