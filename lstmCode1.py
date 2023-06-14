#FUNCIONAL#
#Abre um arquivo CSV com todos os resultados da lotofacil em ordem crescente e salva aplica rede neural para
#predizer os próximos resultados. Esse código é executado 10x e os 10 resultados gerados são salvos
#em um arquivo CSV de nome 'outputRNA.csv'
#
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense, Bidirectional, Dropout
from tensorflow import keras
from keras.optimizers import Adam

batch_size = 100

def execute_prediction():
    # Carregando o arquivo com todos os resultados
    df = pd.read_csv("C:\\Users\\Vandinho\\Documents\\Loteria_Projekt_V2\\Dados_Input\\input_Resultados_Completo_cresc.csv")
    # Exclui as colunas Concurso e Data
    df.drop(['Concurso','Data'],axis=1, inplace=True)

    # Redimensionamento dos dados
    scaler = StandardScaler().fit(df.values)
    transformed_dataset = scaler.transform(df.values)
    transformed_df = pd.DataFrame(data=transformed_dataset, index=df.index)

    # Definição de variáveis
    # Todos os jogos
    number_of_rows = df.values.shape[0]

    # Quantidade de jogos que precisamos retirar da RNA para levar em consideração para a previsão
    window_length = 10

    # Número de bolas
    number_of_features = df.values.shape[1]

    # Definição de X e y para entrada LSTM
    # Pega os 2836 jogos e retira 10 deles para utilizar na previsão
    X = np.empty([ number_of_rows - window_length, window_length, number_of_features], dtype=float)
    y = np.empty([ number_of_rows - window_length, number_of_features], dtype=float)
    for i in range(0, number_of_rows-window_length):
        X[i] = transformed_df.iloc[i : i+window_length, 0 : number_of_features]
        y[i] = transformed_df.iloc[i+window_length : i+window_length+1, 0 : number_of_features]

    # Modelando
    # Iniciando RNA
    model = Sequential()
    # Adicionando a camada de entrada e a camada LSTM
    model.add(Bidirectional(LSTM(240,
                                input_shape = (window_length, number_of_features),
                                return_sequences = True)))
    # Adicionando uma primeira camada Dropout
    model.add(Dropout(0.2))
    # Adicionando uma segunda camada LSTM
    model.add(Bidirectional(LSTM(240,
                                input_shape = (window_length, number_of_features),
                                return_sequences = True)))
    # Adicionando uma segunda camada Dropout
    model.add(Dropout(0.2))
    # Adicionando uma terceira camada LSTM
    model.add(Bidirectional(LSTM(240,
                                input_shape = (window_length, number_of_features),
                                return_sequences = True)))
    # Adicionando uma quarta camada LSTM
    model.add(Bidirectional(LSTM(240,
                                input_shape = (window_length, number_of_features),
                                return_sequences = False)))
    # Adicionando uma terceira camada Dropout
    model.add(Dropout(0.2))
    # Adicionando a primeira camada de saída
    model.add(Dense(59))
    # Adicionando a última camada de saída
    model.add(Dense(number_of_features))

    # Compilando RNA
    model.compile(optimizer=Adam(learning_rate=0.0001), loss ='mse', metrics=['accuracy'])

    # Treinando RNA
    model.fit(x=X, y=y, batch_size=100, epochs=300, verbose=2)

    # Previsão utilizando os último 10 sorteios
    to_predict = df.head(10)
    # to_predict.drop([to_predict.index[-1]],axis=0, inplace=True) # Retira 1 jogo, deixe essa linha no código para
    # análise de resultado reservando o último sorteio

    to_predict = np.array(to_predict)
    scaled_to_predict = scaler.transform(to_predict) # Re-escala os dados

    # Previsão "Exata"
    y_pred = model.predict(np.array([scaled_to_predict]))
    resultado_lotofacil = scaler.inverse_transform(y_pred).astype(int)[0]
    print("A previsão para o resultado da lotofacil eh:", resultado_lotofacil)

    # Salvar o resultado em um arquivo CSV
    try:
        dados_antigos = pd.read_csv('C:\\Users\\Vandinho\\Documents\\Loteria_Projekt_V2\\Dados_Output\\outputRNA.csv')
    except FileNotFoundError:
        dados_antigos = pd.DataFrame()

    novo_dado = pd.DataFrame({'Resultado ': [resultado_lotofacil]})
    dados = pd.concat([dados_antigos, novo_dado])
    dados.to_csv('C:\\Users\\Vandinho\\Documents\\Loteria_Projekt_V2\\Dados_Output\\outputRNA.csv', index=False)

# Executar o código 10 vezes
for _ in range(10):
    execute_prediction()
