sequences = input("Enter a DNA sequences separeted by comas: ").split(",")

counter = [(f"(sequence.strip()).count('A'), (sequence.strip()).count('T'), (sequence.strip()).count('C'), {(sequence.strip()).count('G')}") for sequence in sequences]

print(counter)