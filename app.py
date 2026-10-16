import streamlit as st

import dados

def montar_tabela(jogos):
    tabela = []
    for jogo in jogos:
        # {"jogo": '', "lancamento": '', "preco": '', "donos": '', "desenvolvedora": '', "publicadora":'', "tempo_medio_min": '', "metascore":''}
        linha = {
            "Jogo": jogo["jogo"],
            "Lançamento": jogo["lancamento"],
            "Preço": f"${jogo["preco"]}",
            "Compradores": jogo["donos"],
            "Desenvolvedora": jogo["desenvolvedora"],
            "Publicadora": jogo["publicadora"],
            "Metascore": jogo["metascore"],
            "Tempo medio em minutos": jogo["tempo_medio_min"]
        }
        tabela.append(linha)
    return tabela


def main():
    st.set_page_config(page_title="Dashboard de Jogos da Steam", page_icon="🎮", layout="wide")
    st.title("🎮 Dashboard de Jogos da Steam")

    jogos = dados.ler_csv()
    tabela = montar_tabela(jogos)

    st.dataframe(tabela)


if __name__ == "__main__":
    main()