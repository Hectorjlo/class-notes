# Script for using a file in GFF 
with open("data\cycles\genes.gff") as file:
    for line in file:
        columns = (line.strip()).split("\t")
        size = int(columns[4]) - int(columns[3]) + 1 # The subtraction take -1 nulceotide so we add 1
        print(f"THe gene size is: {size}")
