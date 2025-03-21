apes = ["Pongo pygmaeus", "Pan troglodytes", "Gorilla gorilla"]
# apes will move through the list of apes, one at a time
for ape in apes:
    name_length = len(ape)
    # first_letter will be the first letter of the current ape, because ape is the iteration variable
    first_letter = ape[0]
    print(f"{ape} is an ape. Its name starts with {first_letter}")
    print(f"Its name has {name_length} letters")

# Or

for ape in apes:
    print(f"{ape} is an ape. Its name starts with {ape[0]}")
    print(f"Its name has {len(ape)} letters")