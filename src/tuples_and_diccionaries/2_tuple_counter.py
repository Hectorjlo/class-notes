# This script takes a given sequence, create a tuple with it and count how many bases are in the DNA sequence


sequence = tuple("ATCGATCGTA")

print("A:", sequence.count("A"), end="\t")
print("T:", sequence.count("T"), end="\t")
print("C:", sequence.count("C"), end="\t")
print("G:", sequence.count("G"))