"""
Module to read a FASTA file
"""

from pathlib import Path


def read_fasta(fasta_path):
    path = Path(fasta_path)
    if not path.is_file():
        print(f"[ERROR] File not found: {fasta_path}")
        return {}

    sequences = {}
    actual_id = None
    with open(fasta_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                actual_id = line[1:].strip()
                sequences[actual_id] = ''
            else:
                if actual_id:
                    sequences[actual_id] += line.upper()
    return sequences