# Script for printing a sequence only it has a stop codon in it
sequences = (input("Enter a sequences of DNA separated by comas: ").split(","))



stop_codon_found = [sequence.strip() for sequence in sequences if "TAA" in sequence or "TAG" in sequence or "TGA" in sequence]

print(stop_codon_found)