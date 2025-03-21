sequence = "ACTTGACATTC"

for i, base, in enumerate(sequence):
    print(f"Base {i}: {base}")

# Output
# Base 0: A
# Base 1: C
# Base 2: T
# Base 3: T

# Zip function

base = "ATGC"
complement = "TACG"

for base, complement in zip(base, complement):
    print(f"{base} <-> {complement}")