#Projeto
#o desafio é conseguir prever as vendas que vamos ter em determinado periodo com 
#base nos gastos em anúcios nas 3 grandes redes que a empresa investe: tv jornal e radio
#Ciencias de dados, analise exploratoria, inteligencia artificial, analise de modelos
import pandas as pd 

tabela = pd.read_csv("Dados/advertising.csv")
display(tabela)




#Analise exploratoria
#vamos tentar vizualizar como as informações de cada item estão destribuidas
#vamos ver a correlação entre cada um dos itens 
import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(tabela.corr(), annot=True, cmap="Wistia")
plt.show

sns.pairplot(tabela)
plt.show


#separando em dados de treino e dados de teste
from sklearn.model_selection import train_test_split

y = tabela["Vendas"]
x = tabela.drop("Vendas", axis=1)

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1)


#modelo da inteligencia artificiais
#regressão linear
#randomforest(arvore de decisão)
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

#cria as inteligencias artificiais
modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

#treina as inteligencias artificiais
modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)


from sklearn import metrics

#criar as previsões 
previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoresdecisao.predict(x_teste)

#comparar os modelos
print(metrics.r2_score(y_teste, previsao_regressaolinear))
print(metrics.r2_score(y_teste, previsao_arvoredecisao))
'''0.9071151423684272
   0.9634248429820929''' 


#visualização grafica das previsões 
tabela_auxiliar = pd.DataFrame()
tabela_auxiliar["y_teste"] =y_teste
tabela_auxiliar["previsao ArvoresDecisão"] = previsao_arvoredecisao
tabela_auxiliar["previsao Regressao Linear"] = previsao_regressaolinear

plt.figure(figsize=(15,5))
sns.lineplot(data=tabela_auxiliar)
plt.show()


#esse grafico mostra quem é mais importante da base de dados 
sns.barplot (x=x_treino.columns, y=modelo_arvoresdecisao.feature_importances_)
plt.show()
