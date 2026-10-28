# 🎮 Dashboard Jogos Steam

Este projeto é um dashboard interativo desenvolvido em Python utilizando o Streamlit, focado em analisar e exibir dados sobre jogos na plataforma Steam.

**Membros da Equipa:** Alex Sandro, Northon V.
**Dataset utilizado:** `jogos-steam.csv` e dados da [SteamSpy](https://steamspy.com/year/)
**Aplicação publicada:** [Link para o App no Streamlit](https://jogos-steam.streamlit.app/)

---

## 🚀 Funcionalidades Implementadas

O projeto cumpre os seguintes requisitos:

- [x] Leitura de dados a partir de um ficheiro CSV.
- [x] Conversão e tratamento dos tipos de colunas (numéricas, texto, etc.).
- [x] Exibição de métricas principais do dataset (Maior publicadora, Jogo melhor avaliado e Jogo com maior tempo médio).
- [x] Classificação e exibição de registos em faixas através de uma coluna numérica na tabela (Metascore).
- [x] Tabela de dados interativa com nomes de colunas formatados e legíveis.
- [x] Motor de busca por texto (case-insensitive) para encontrar jogos específicos.
- [x] Filtro dinâmico por categoria/desenvolvedora, extraído diretamente dos dados, incluindo a opção "Todas".
- [x] Funcionamento simultâneo e integrado da busca por texto e do filtro por categoria.
- [x] Exibição de mensagem de aviso quando nenhum resultado é encontrado na busca.
- [x] Código estruturado e organizado em funções e módulos (`app.py` e `dados.py`).
- [x] Aplicação publicada e acessível no Streamlit Community Cloud.

### 🌟 Funcionalidade Extra
**Recomendação de Jogo:** Um botão interativo ("❓ Recomendar um jogo aleatório") localizado abaixo da tabela principal que, ao ser clicado, seleciona e exibe as informações detalhadas de um jogo aleatório do catálogo para o utilizador.

---

## 🛠️ Como rodar o projeto localmente

Siga os passos abaixo no seu terminal (especialmente configurado para Windows PowerShell):

1. **Criar o ambiente virtual:**
   ```powershell
   python -m venv .venv
   ```

2. **Permitir a execução de scripts no PowerShell e ativar o ambiente:**
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\.venv\Scripts\Activate.ps1
   ```

3. **Instalar as dependências do projeto:**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Executar a aplicação:**
   ```powershell
   streamlit run app.py
   ```
