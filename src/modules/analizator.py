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
ruta_entrada = "data/secuencias.fasta"
ruta_salida = "output/resultados.tsv"

secuencias = read_fasta(ruta_entrada)

if not secuencias:
    print("[INFO] No se procesó ninguna secuencia.")
else:
    resultados = {}
    for gen_id, sec in secuencias.items():
        if not validate_sequence(sec):
            print(f"[ADVERTENCIA] La secuencia del gen '{gen_id}' contiene bases no válidas y será omitida.")
            continue

        bases = base_counter(sec)
        gc = calculate_gc_content(sec)
        resultados[gen_id] = {
            "longitud": len(sec),
            "A": bases["A"],
            "T": bases["T"],
            "G": bases["G"],
            "C": bases["C"],
            "GC%": gc
        }

    if resultados:
        export_tsv(resultados, ruta_salida)
        print(f"[OK] Resultados guardados en: {ruta_salida}")
    else:
        print("[INFO] No se generaron resultados válidos para exportar.")

# --- Pruebas simples con assert para verificar funciones clave ---
assert base_counter("ATGC") == {"A": 1, "T": 1, "G": 1, "C": 1}, "Error en contar_bases()"
assert calculate_gc_content("ATGC") == 50.0, "Error en calcular_gc()"
assert validate_sequence("ATGC") is True, "Error en validar_secuencia() con secuencia válida"
assert validate_sequence("ATGN") is False, "Error en validar_secuencia() con caracteres inválidos"
