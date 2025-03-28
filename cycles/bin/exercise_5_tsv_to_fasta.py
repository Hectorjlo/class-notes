with open("cycles/data/dna_sequences.txt", "r") as input_file, open("cycles/dna_sequences.fa", "w") as output_file:
    for line in input_file:
        columns = (line.strip()).split("\t")
        

        output_file.write(f">{columns[0]}\n")  
        output_file.write(f"{columns[1].upper()}\n")  
    
    # or

    # for line in input_file:
    #    ids, sequence = line.strip().split("\t")
    #    output_file.write(f">{ids}\n{sequence.upper()}\n")