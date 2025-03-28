sequences = input("Enter a sequence of numbers separated by comas: ").split(",")

reverse_sequence = [(sequences.strip())[::-1] for sequences in sequences]

print(f"Reversed sequence: {reverse_sequence}")