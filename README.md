
# Dashboard Financeiro

Este é um projeto de um Dashboard Financeiro desenvolvido para estudos em desenvolvimento de software. O objetivo do projeto é permitir que os usuários visualizem dados financeiros de forma interativa, com gráficos e filtros para análise.

# Funcionalidades

- Gráfico de Lucro Mensal: Exibe o lucro mensal ao longo do tempo.
- Gráfico de Receita vs Gastos: Compara os dados de receita e gastos em um gráfico de barras.
- Gráfico de Pizza de Gastos: Mostra a distribuição dos gastos mensais.
- Filtros Interativos:
- Intervalo de Meses: O usuário pode selecionar o intervalo de meses a ser visualizado.
- Seleção de Métricas: O gráfico de linha permite que o usuário escolha entre visualizar "Lucro", "Receita" ou "Gastos".
# Tecnologias Utilizadas
- Python: Linguagem principal para desenvolvimento.
- Dash: Framework utilizado para criação do dashboard interativo.
- Plotly: Biblioteca usada para gerar gráficos interativos.
- Pandas: Usado para manipulação e análise de dados.
- HTML/CSS (Dash): Para estruturação e design básico da interface.
# Como Rodar o Projeto
- Pré-requisitos
- Python 3.x instalado em sua máquina.
- As seguintes bibliotecas Python instaladas:
  - dash 
  - plotly
  - pandas
## Passos para Execução

- Clone o repositório:
  - git clone https://github.com/tuliorav/dashboard_financeiro.git
- Navegue até o diretório do projeto:
  - cd dashboard_financeiro
- Instale as dependências:
  - pip install -r requirements.txt
- Execute o projeto:
  - python app.py
- Abra o navegador e vá até http://127.0.0.1:8050 para visualizar o dashboard.

# Estrutura do Projeto
dashboard_financeiro/

├── app.py              # Arquivo principal do projeto  
├── data/               # Pasta para armazenar os dados  
│   └── financeiro.csv  # Dados de exemplo  
└── README.md           # Este arquivo

# Considerações Finais
Este projeto foi desenvolvido como uma primeira experiência em desenvolvimento de dashboards interativos, utilizando as tecnologias Python, Dash e Plotly. A ideia foi criar uma solução simples, mas que oferece funcionalidades essenciais para visualização de dados financeiros. Este é apenas o começo, e futuras melhorias, como mais interatividade e adição de mais funcionalidades, serão feitas conforme o aprendizado e ganho de expêriencia nos estudos.