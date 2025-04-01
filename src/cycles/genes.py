# Using reversed funtion to print the list the oppossite way
genes = ["crp", "recA", "lacZ", "galK", "galT", "galE", "mglB", "mglC"]

for gene in reversed(genes):
    print(f"The gen name is:{gene}")

# An other way
#for gene in genes[::-1]:
#    print(f"The gen name is:{gene}")