
def base_counter(dna):
    bases = "ATCG"
    dna = dna.upper().strip()

    for base in bases:
        frecuency_base = dna.count(base)
        print(f"{base}: {frecuency_base}")


base_counter("TATATTATATAT")