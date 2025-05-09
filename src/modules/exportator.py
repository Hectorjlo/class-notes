from pathlib import Path

def export_tsv(results, output_path):
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w') as f:
        f.write("ID\tLenght\tA\tT\tG\tC\tGC%\n")
        for gen_id, data in results.items():
            f.write(f"{gen_id}\t{data['lenght']}\t{data['A']}\t{data['T']}\t{data['G']}\t{data['C']}\t{data['GC%']}\n")