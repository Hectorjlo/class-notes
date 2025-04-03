# Script for counting each character of a file, not taking the lines starting with ">" but their contents
data_file = "data/exercises/fasta_sequence.txt"

with open(data_file, "r") as input_file:
    lines = input_file.readlines()

filtered_lines = [line for line in lines if line.startswith(">")]
# print(len(filtered_lines))
print(f"Total number of sequences: {len(filtered_lines)}")
    
