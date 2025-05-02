def validate_sequence(sequence):
    valid_bases = {"A", "T", "G", "C"}
    return all(base in valid_bases for base in sequence)