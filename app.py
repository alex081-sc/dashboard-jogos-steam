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

def listar_desenvolvedoras(jogos):
    desenvolvedoras = []
    for jogo in jogos:
        if jogo["desenvolvedora"] not in desenvolvedoras:
            desenvolvedoras.append(jogo["desenvolvedora"])
    return desenvolvedoras

def filtrar_por_desenvolvedora(opcao, jogos):
    jogos_categoria = []
    if opcao == "Todas":
        return jogos
    for jogo in jogos:
        if opcao in jogo["desenvolvedora"]:
            jogos_categoria.append(jogo)
    return jogos_categoria

def buscar_jogos(busca, jogos):
    jogos_busc = []
    busca_padrao = busca.lower().strip()
    for jogo in jogos:
        jogo_padrao = jogo["jogo"].lower().strip()
        if busca_padrao in jogo_padrao:
            jogos_busc.append(jogo)
    return jogos_busc

def main():
    st.set_page_config(page_title="Dashboard de Jogos da Steam", page_icon="🎮", layout="wide")
    st.title("🎮 Dashboard de Jogos da Steam")

    jogos = dados.carrega_jogos()
    

    col_busca, col_desenv = st.columns(2)

    busca = col_busca.text_input(label="Nome do Jogo", type="search", live=True)
    opcao = col_desenv.selectbox("Filtrar por desenvolvedoras",["Todas"] + listar_desenvolvedoras(jogos))

    jogos_filtrados = filtrar_por_desenvolvedora(opcao, jogos)
    jogo_buscado = buscar_jogos(busca, jogos_filtrados)

    dados_tabela = montar_tabela(jogo_buscado)

    if len(dados_tabela) == 0:
        st.warning("Nenhum jogo encontrado!")
    else:
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