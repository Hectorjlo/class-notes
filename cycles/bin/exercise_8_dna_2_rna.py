sequences = input("Enter DNA sequences separated by comas: ").split(",")

rna_sequences = [(sequence.strip()).replace("T", "U") for sequence in sequences]

print(rna_sequences)