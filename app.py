# Importações necessárias
import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Carregar os dados
data = pd.read_csv('data/financeiro.csv')

# Inicializar o app
app = dash.Dash(__name__)

# Layout do app
app.layout = html.Div([
    html.H1("Dashboard Financeiro", style={"text-align": "center"}),

    # Filtro de intervalo de meses
    html.Label("Selecione o intervalo de meses:"),
    dcc.RangeSlider(
        id='mes-slider',
        min=0,
        max=len(data) - 1,
        marks={i: mes for i, mes in enumerate(data['Mês'])},
        value=[0, len(data) - 1]
    ),

    # Dropdown para selecionar a métrica no gráfico de linha
    html.Label("Selecione a métrica para o gráfico de linha:"),
    dcc.Dropdown(
        id='metrica-dropdown',
        options=[
            {'label': 'Lucro', 'value': 'Lucro'},
            {'label': 'Receita', 'value': 'Receita'},
            {'label': 'Gastos', 'value': 'Gastos'}
        ],
        value='Lucro',
        clearable=False
    ),

    # Gráficos
    dcc.Graph(id='grafico-linha'),
    dcc.Graph(id='grafico-barras'),
    dcc.Graph(id='grafico-pizza')
])

# Callbacks para atualizar os gráficos com base no filtro e na métrica
@app.callback(
    [Output('grafico-linha', 'figure'),
     Output('grafico-barras', 'figure'),
     Output('grafico-pizza', 'figure')],
    [Input('mes-slider', 'value'),
     Input('metrica-dropdown', 'value')]
)
def atualizar_graficos(intervalo, metrica):
    # Filtrar os dados com base no intervalo de meses selecionado
    data_filtrada = data.iloc[intervalo[0]:intervalo[1] + 1]

    # Criar gráficos atualizados
    fig_linha = px.line(data_filtrada, x="Mês", y=metrica, title=f"{metrica} Mensal")
    fig_barras = px.bar(
        data_filtrada, 
        x="Mês", 
        y=["Receita", "Gastos"], 
        title="Receita vs Gastos Mensais",
        barmode='group'
    )
    fig_pizza = px.pie(
        data_filtrada, 
        values="Gastos", 
        names="Mês", 
        title="Distribuição de Gastos"
    )
    return fig_linha, fig_barras, fig_pizza

# Rodar o servidor
if __name__ == '__main__':
    app.run_server(debug=True)
