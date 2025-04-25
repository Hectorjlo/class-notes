def at_counter(dna, significant_figures):
    dna = dna.upper().strip()
    lenght = len(dna)
    a_count = dna.count("A")
    t_count = dna.count("T")
    at_content = ((a_count + t_count) / lenght)
    return round(at_content, significant_figures)

result = at_counter("atatatata", 1)
print(result)

result = at_counter(significant_figures=5, dna="AGCTAGCTA")
print(result)

result = at_counter(dna="ATCGATCGATCGACG", significant_figures=6)
print(result)
