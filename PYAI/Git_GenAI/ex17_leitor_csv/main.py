# EX. 17: Leitor de CSV
# Lê alunos.csv com notas, calcula média e salva resultado em resultado.csv.

import csv

entrada = "alunos.csv"
saida = "resultado.csv"

with open(entrada, newline="", encoding="utf-8") as f_in, \
     open(saida, "w", newline="", encoding="utf-8") as f_out:

    reader = csv.DictReader(f_in)
    fieldnames = ["nome", "media", "status"]
    writer = csv.DictWriter(f_out, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        notas = [float(row[f"nota{i}"]) for i in range(1, 5)]
        media = sum(notas) / len(notas)
        status = "aprovado" if media >= 7 else "reprovado"
        writer.writerow({"nome": row["nome"], "media": f"{media:.2f}", "status": status})
        print(f"{row['nome']}: média {media:.2f} -> {status}")

print(f"\nResultado salvo em {saida}")
