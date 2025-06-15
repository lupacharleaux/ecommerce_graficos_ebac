import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Abrindo arquivo csv para verificar os dados
df = pd.read_csv('ecommerce_estatistica.csv')

# Selecionando os campos que vou trabalhar
df = df[['Nota', 'N_Avaliações', 'Desconto', 'Gênero', 'Temporada', 'Qtd_Vendidos', 'Preço', 'Marca_Cod', 'Material_Cod', 'Temporada_Cod', 'Qtd_Vendidos_Cod', 'Marca_Freq','Material_Freq']]
print(df.head().to_string())

# Histograma
plt.figure(figsize=(10, 6))
plt.hist(df['Preço'], bins=100, color='blue', alpha=0.8)
plt.title('Histograma - Distribuição de Preço de Produtos')
plt.xlabel('Preço')
plt.xticks(ticks=range(0, int(df['Preço'].max())+75, 75))
plt.ylabel('Quantidade')
plt.grid(True)
plt.show()
plt.savefig('histograma.png')

# Gráfico de Dispersão
plt.hexbin(df['Preço'], df['Desconto'], gridsize=20, cmap='Blues')
plt.colorbar(label='Contagem dentro do bin')
plt.xlabel('Preço')
plt.ylabel('Desconto')
plt.title('Dispersão de Preço e Desconto')
plt.show()
plt.savefig('dispersao.png')

# Mapa de Calor
corr = df[['Nota', 'N_Avaliações']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Nota e Número de Avaliações')
plt.show()
plt.savefig('heatmap.png')

# Gráfico de barra com PLT
x = df['Qtd_Vendidos'].value_counts().index
y = df['Qtd_Vendidos'].value_counts().values

plt.figure(figsize=(10,6))
plt.bar(x, y, color='Blue')
plt.title('Divisão de Qtd Vendidos')
plt.xlabel('Nível de Vendas')
plt.ylabel('Quantidade')
plt.show()
plt.savefig('barra.png')

# Gráfico de Pizza
plt.figure(figsize=(10,6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title('Distribuição de Níveis de Venda')
plt.show()
plt.savefig('pizza.png')

# Gráfico de Densidade
plt.figure(figsize=(10,6))
sns.kdeplot(df['Preço'], fill=True, color='Blue')
plt.title('Densidade de Preço')
plt.xlabel('Preço')
plt.show()
plt.savefig('densidade.png')

# Gráfico de Regressão
sns.regplot(x='Preço', y='Qtd_Vendidos_Cod', data=df, color='#371eb8', scatter_kws={'alpha': 0.5, 'color': '#674fde'})
plt.title('Regressão de Preço por Quantidade Vendidos')
plt.xlabel('Preço')
plt.ylabel('Qtd Vendidos')
plt.show()
plt.savefig('regressao.png')