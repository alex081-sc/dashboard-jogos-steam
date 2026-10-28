import streamlit as st
import pandas as pd
import random as rd

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

def sortear_jogo(jogos): # funcao extra
    return rd.choice(jogos)
    

def main():
    # estilização do fundo da dashboard
    st.markdown(
    """
    <style>
    .stAppViewContainer {
        
        background-image: linear-gradient(
            to bottom, 
            rgba(0, 0, 0, 0.6), 
            rgba(20, 30, 48, 10)
        ), 
        url("https://static0.gamerantimages.com/wordpress/wp-content/uploads/2024/09/steam.jpg");
        
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
    ) 

    st.set_page_config(page_title="Dashboard de Jogos da Steam", page_icon="🎮", layout="wide")
    st.title("🎮 Dashboard de Jogos da Steam")

    jogos = dados.carrega_jogos()

    col1, col2, col3 = st.columns(3)
    
    jogo_mais_longo, tempo_jogo = dados.jogo_mais_longo(jogos)
    nota_jogo, melhor_jogo = dados.melhor_jogo(jogos)
    maior_empresa, qntd_jogos_empresa = dados.empresa_com_mais_jogos(jogos)
    
    col1.metric("Publicadora/Empresa com mais jogos lançados", maior_empresa)
    col1.caption(f"Quantidade de jogos: {qntd_jogos_empresa}")
    
    col2.metric("Jogo melhor avaliado", melhor_jogo)
    col2.caption(f"Nota: {nota_jogo} no Metascore")

    col3.metric("Jogo com maior tempo médio", jogo_mais_longo)
    col3.caption(f"Tempo médio: {tempo_jogo} Minutos")
    
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
    
    if st.button("❓ Recomendar um jogo aleatório"):
            jogo_sorteado = sortear_jogo(jogos)

            
            st.subheader(f"🎮 Jogo recomedado: {jogo_sorteado['jogo']}")
            

            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Preço", f"${jogo_sorteado['preco']}")
            col2.metric("Desenvolvedora", jogo_sorteado['desenvolvedora'])
            col3.metric("Metascore", f"{jogo_sorteado['metascore']}/100")
            col4.metric("Lançamento", jogo_sorteado['lancamento'])
            st.image("https://static.wikitide.net/nicosnextbotswiki/7/74/Nextbot_steamhappy.png", width=50)

if __name__ == "__main__":
    main()
    