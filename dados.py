"""Leitura dos arquivos CSV do projeto."""

from pathlib import Path
import csv


PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "jogos-steam.csv"

def ler_csv():
    """Le o csv de jogos e devolve uma lista de dicionarios.
    """
    jogos = []
    try:
        with open(CAMINHO_LIVROS, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                jogos.append(linha)
    except FileNotFoundError:
        print("Arquivo de jogos nao encontrado")
    except Exception as error:
        print("Erro: ", error)

    return jogos

if __name__ == "__main__":
    jogos = ler_csv()
    print()