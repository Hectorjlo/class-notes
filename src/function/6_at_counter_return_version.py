def at_counter(dna, significant_figures=2):
    """
    Calculates the AT content of a given sequence of DNA,
    it rounds up of a precise number of significant figures

    Parameters:
    dna (str): Sequence of DNA (ex. 'ATGCGC')
    significant_figures (int, opcional): number of significant figures (default = 2)

    Return:
    float: Content AT round up
    """
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

# TESTING OF AT CONTENT
assert at_counter("ATCG", 1) == 0.5

at_counter()