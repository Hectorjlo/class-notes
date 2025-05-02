def base_counter(sequence):
    bases = {"A": 0, "T": 0, "G": 0, "C": 0}
    for base in sequence:
        if base in bases:
            bases[base] += 1
    return bases


def calculate_gc_content(sequence):
    total = len(sequence)
    if total == 0:
        return 0.0
    g = sequence.count("G")
    c = sequence.count("C")
    return round((g + c) / total * 100, 2)