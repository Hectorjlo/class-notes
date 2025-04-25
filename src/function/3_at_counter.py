
def at_counter(dna):
    dna = dna.upper().strip()
    lenght = len(dna)
    a_count = dna.count("A")
    t_count = dna.count("T")
    at_content = ((a_count + t_count) / lenght)
    print(f"AT content is {at_content:.2f}% of the sequence")

at_counter("atatatata")
at_counter("CGAGCAGTACG")
