# Script for printing the first 3 characters of a sequence (first codon)
sequences = (input("Enter sequences of DNA separated by comas: ")).split(",")


# Comprehension list

start_codons = [sequence.strip()[:3] for sequence in sequences]

print(start_codons)
    