# Script for a given forward sequence printing the reverse sequence 
sequences = input("Enter a sequence of DNA separated by comas: ").split(",")

reverse_sequence = [(sequences.strip())[::-1] for sequences in sequences]

print(f"Reversed sequence: {reverse_sequence}")