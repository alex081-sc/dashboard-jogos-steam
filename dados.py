"""Leitura dos arquivos CSV do projeto."""

from pathlib import Path
import csv


PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "jogos-steam.csv"

def ler_csv():
    """Le o csv de jogos e devolve uma lista de dicionarios.
    {"jogo": '', "lancamento": '', "preco": '', "donos": '', "desenvolvedora": '', "publicadora":'', "tempo_medio_min": '', "metascore":''}
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

def converte_preco(preco):
    preco = preco.replace(".", ".")
    if preco == "NA":
        return 0
    return float(preco)

def converte_nota(nota):
    return int(nota)

def converte_tempo(tempo):
    if tempo == "NA":
        return 0
    return int(tempo)

def prepara_jogos(jogos):
    jogos_prep = []
    for jogo in jogos:
        jogo_prep = {
            "jogo": jogo["jogo"],
            "lancamento": jogo["lancamento"],
            "preco": converte_preco(jogo["preco"]),
            "donos": jogo["donos"],
            "desenvolvedora": jogo["desenvolvedora"],
            "publicadora": jogo["publicadora"],
            "tempo_medio_min": converte_tempo(jogo["tempo_medio_min"]),
            "metascore": converte_nota(jogo["metascore"])
        }
        jogos_prep.append(jogo_prep)
    return jogos_prep

def carrega_jogos():
    return(prepara_jogos(ler_csv()))

if __name__ == "__main__":
    jogos = carrega_jogos()
    for jogo in jogos:
        print(type(jogo["jogo"]))
        print(type(jogo["lancamento"]))
        print(type(jogo["preco"]))
        print(type(jogo["donos"]))
        print(type(jogo["desenvolvedora"]))
        print(type(jogo["publicadora"]))
        print(type(jogo["tempo_medio_min"]))
        print(type(jogo["metascore"])) 
        break