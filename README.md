# Dashboard Jogos Steam

**Membros:** Alex Sandro, Northon V.

**Dataset:** jogos-steam.csv + https://steamspy.com/year/

**App publicado:** https://...streamlit.app
## Funcionalidades
- [1] Leitura do CSV
- [2] Conversão das colunas
- [3] Mostrar no mínimo 3 métricas sobre o dataset (Maior publicadora, Jogo melhor avaliado e Jogo com maior tempo médio)
- [4] Classificar os registros em faixas a partir de uma coluna numérica e mostrar a faixa na tabela
- [5] Uma tabela com os dados e nomes de coluna legíveis
- [6] Uma busca por texto que não diferencie maiúsculas de minúsculas
- [7] Um filtro por categoria, com as opções dos próprios dados (sem escrever à mão) e uma opção para mostrar todos (Feito com as desenvolvedoras)
- [8] Busca e filtro funcionando juntos
- [9] Uma mensagem quando nenhum resultado for encontrado
- [10] Código organizado em funções e módulos, com nomes que façam sentido no tema do grupo
- [11] App publicado no Streamlit Community Cloud

## Funcionalidade extra
Função de recomende um jogo. Há um botão escrito "Me recomende um jogo" embaixo da tabela, que ao ser clicado vai mostrar as informações de um jogo aleatório para o usuário.
## Como rodar

python -m venv .venv

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

.venv\Scripts\Activate.ps1

pip install -r requirements.txt

streamlit run app.py
