#take each line and remove the first 14 characters

with open("cycles/4_input_adapters.txt", "r") as file, open("cycles/4_output_adapters.txt", "w") as output_file:
    for line in file:
        no_primers = (line.strip())[14:]  # Remove the first 14 characters

        output_file.write(f"{no_primers}\n")  # Write the modified line to the output file
        