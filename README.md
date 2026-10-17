# Dashboard Jogos Steam

**Membros:** Alex Sandro, Northon V.

**Dataset:** jogos-steam.csv + https://steamspy.com/year/

**App publicado:** https://...streamlit.app
## Funcionalidades
- [x] Leitura do CSV
- [x] Conversão das colunas
- [x] ... (os 11 itens do enunciado, marcados)

## Funcionalidade extra
Função de recomende um jogo. Vai ter um botão escrito "Me recomende um jogo", que ao ser clicado vai mostrar as informações de um jogo aleatório.
## Como rodar

python -m venv .venv

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

.venv\Scripts\Activate.ps1

pip install -r requirements.txt

streamlit run app.py
