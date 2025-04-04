import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent


try:
    with open(ROOT_PATH / "usuarios.csv", "w", newline='', encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["id", "nome"])
        escritor.writerow(["1", "Maria"])
        escritor.writerow(["2", "João"])
except IOError as e:
    print(f"Erro ao criar o arquivo. {e}")

