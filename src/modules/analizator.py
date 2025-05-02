"""
==================================================
🧬 Analizador de Secuencias Genéticas - FASTA
==================================================

Este programa permite analizar secuencias de genes almacenadas en un archivo
FASTA. Realiza lo siguiente:

✅ Lee el archivo FASTA
✅ Verifica que las secuencias contengan solo bases A, T, G, C
✅ Calcula frecuencia de bases
✅ Calcula contenido GC
✅ Exporta resultados a un archivo .tsv

🔧 Requisitos:
- El archivo de entrada debe estar en: data/secuencias.fasta
- Los resultados se guardan en: output/resultados.tsv

▶️ Ejecución:

    python analizador.py

Autor: Tu Nombre
Fecha: 2025

--------------------------------------------------
"""

from fasta_utils import read_fasta
from bioestadistics import base_counter, calculate_gc_content
from exportator import export_tsv
from validator import validate_sequence




# --- Inicio del programa ---
input_path = "data\modules\secuencias.fasta"
output_path = "results/modules/resultados.tsv"

sequences = read_fasta(input_path)

if not sequences:
    print("[INFO] No sequence was processed")
else:
    results = {}
    for gen_id, sec in sequences.items():
        if not validate_sequence(sec):
            print(f"[ADVERTENCIA] The sequence of the gene '{gen_id}' contains no valid bases and would be ommited.")
            continue

        bases = base_counter(sec)
        gc = calculate_gc_content(sec)
        results[gen_id] = {
            "lenght": len(sec),
            "A": bases["A"],
            "T": bases["T"],
            "G": bases["G"],
            "C": bases["C"],
            "GC%": gc
        }

    if results:
        export_tsv(results, output_path)
        print(f"[OK] Results saved in: {output_path}")
    else:
        print("[INFO] Not valid results were generated hence were not exported.")

# --- Pruebas simples con assert para verificar funciones clave ---
assert base_counter("ATGC") == {"A": 1, "T": 1, "G": 1, "C": 1}, "Error in base_counter()"
assert calculate_gc_content("ATGC") == 50.0, "Error in calculate_gc_content()"
assert validate_sequence("ATGC") is True, "Error in validate_sequence() with invalid sequence"
assert validate_sequence("ATGN") is False, "Error in validate_sequence() with invalid characters"
