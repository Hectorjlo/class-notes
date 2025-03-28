sequences = (input("Enter a sequence of numbers separated by spaces: ")).split(",")

# print(sequences)

# Comprehension list

start_codons = [sequence.strip()[:3] for sequence in sequences]

print(start_codons)
    