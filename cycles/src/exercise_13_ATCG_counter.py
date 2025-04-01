sequences = input("Enter a DNA sequences separeted by comas: ").split(",")

counter = [f"A: {sequence.strip().count('A')}, T: {sequence.strip().count('T')}, C: {sequence.strip().count('C')}, G: {sequence.strip().count('G')}" for sequence in sequences]

print(counter)