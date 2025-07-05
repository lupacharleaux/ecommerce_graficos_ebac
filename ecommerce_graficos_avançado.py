import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dash import Dash, html, dcc

def criar_graficos(df):
    # Grafíco de Histograma
    fig1 = px.histogram(df, x='Preço', nbins=30, title='Histograma - Distribuição de Preços de Produtos')

    # Gráfico de Dispersão
    fig2 = plt.hexbin(df['Preço'], df['Desconto'], gridsize=20, cmap='Blues')
    plt.colorbar(label='Contagem dentro do bin')
    plt.xlabel('Preço')
    plt.ylabel('Desconto')
    plt.title('Dispersão de Preço e Desconto')
    plt.show

    # Mapa de Calor
    corr = df[['Nota', 'N_Avaliações']].corr()
    fig3 = px.imshow(corr, text_auto=True, aspect='auto', color_continuous_scale='Viridis', title='Correlação Nota e Número de Avaliações')

    # Gráfico de barra
    fig4 = px.bar(df, x='Nota', y='Qtd_Vendidos', color='N_Avaliação', barmode='group', color_discrete_sequence=px.colors.qualitative.Bold, opacity=1)
    fig4.update_layout(
        title='Divisão de Qtd Vendidos por Notas e Nº de Avaliações',
        xaxis_title='Nota',
        yaxis_title='Qtd Vendidos',
        legend_title='Nº de Avaliações',
        plot_bgcolor = 'rgba(222, 255, 253, 1)',  # Fundo Interno
        paper_bgcolor = 'rgba(186, 245, 241, 1)'  # Fundo externo
    )

    # Gráfico de Pizza
    fig5 = px.pie(df, names='Qtd_Vendidos', color='Qtd_vendidos', hole=0.2, color_discrete_sequence=px.colors.sequential.ice)
    fig5.update_layout(
        title='Distribuição de Níveis de Venda',
        legend_title='Níveis de Vendas'
    )

    # Gráfico de Densidade
    fig6 = plt.figure(figsize=(10, 6))
    sns.kdeplot(df['Preço'], fill=True, color='Blue')
    plt.title('Densidade de Preço')
    plt.xlabel('Preço')
    plt.show

    # Gráfico de Regressão
    fig7 = sns.regplot(x='Preço', y='Qtd_Vendidos_Cod', data=df, color='#371eb8', scatter_kws={'alpha': 0.5, 'color': '#674fde'})
    plt.title('Regressão de Preço por Quantidade Vendidos')
    plt.xlabel('Preço')
    plt.ylabel('Qtd Vendidos')
    plt.show

    return fig1, fig2, fig3, fig4, fig5, fig6, fig7

def criar_app(df):
    #Criar App
    app = Dash(__name__)

    fig1, fig2, fig3, fig4, fig5, fig6, fig7 = criar_graficos(df)

    app.layout = html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig4),
        dcc.Graph(figure=fig5),
        dcc.Graph(figure=fig6),
        dcc.Graph(figure=fig7),
    ])
    return app

df = pd.read_csv('ecommerce_estatistica.csv')

# Executa App
if __name__ == '__main__':
   app = criar_app(df)
   app.run(debug=True, port=8050) # Defaut 8050
