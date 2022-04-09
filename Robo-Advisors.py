import pandas as pd
from sklearn.feature_selection import  SelectKBest
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt



dataset = pd.read_excel('forex.xlsx')

dataset.head()


dataset.dtypes


dataset['time'] = pd.to_datetime(dataste['time'], format = '%Y,%m,%d')


#criando novos campos de media móvies
dataset['mm5d'] = dataset['close'].rolling(5).mean()
dataset['mm21d'] = dataset['close'].rolling(21).mean()

dataset['close'] = dataset['close'].shift(-1)
dataset.head()


dataset.dropna(inplace=True)
dataset
qtd_linhas = len(dataset)
qtd_linhas_treino = qtd_linhas - 550
qtd_linhas_teste = qtd_linhas - 15
qtd_linhas_validacao = qtd_linhas_treino - qtd_linhas_teste

info = (
    f"Linhas de Treino = 0:{qtd_linhas_treino}"
    f"Linhas de Teste = {qtd_linhas_treino}:{qtd_linhas_teste}"
    f"Linhas de Teste = {qtd_linhas_teste}:{qtd_linhas_teste}"
    )


info

#reindexando o DataFrame
dataset = dataset.reset_index(drop=True)
dataset

#separando as features e lables
features = dataset.drop(['time','real_volume'],1)
labels = dataset['close']

features_list = ('open', 'tick_volume', 'spread', 'mm5d','mm21d')
