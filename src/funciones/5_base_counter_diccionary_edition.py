def count_bases(dna):
    dna = dna.upper().strip()
    counter = {
        'A': dna.count('A'),
        'T': dna.count('T'),
        'C': dna.count('C'),
        'G': dna.count('G')
    }
    return counter

dna = "ATCGTACGTA"
result = count_bases(dna)