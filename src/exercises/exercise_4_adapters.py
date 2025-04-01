# script for removing first 14 characters of an external archive.
with open("data/exercises/4_input_adapters.txt", "r") as file, open("results/exercises/4_output_adapters.txt", "w") as output_file:
    #take each line and remove the first 14 characters
    for line in file:
        no_primers = (line.strip())[14:]  # Remove the first 14 characters

        output_file.write(f"{no_primers}\n")  # Write the modified line to the output file
        