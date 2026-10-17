import streamlit as st
import pandas as pd

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

    jogos = dados.carrega_jogos()
    dados_tabela = montar_tabela(jogos)

    tabela = pd.DataFrame(dados_tabela)
    st.data_editor(
        tabela,
        column_config={
        f"Metascore": st.column_config.ProgressColumn(
                "Avaliação metascore",
                help="Avaliação metascore",
                format="%f",
                min_value=0,
                max_value=100,
                color="auto"
            ),
        },
    hide_index=True,
)

if __name__ == "__main__":
    main()