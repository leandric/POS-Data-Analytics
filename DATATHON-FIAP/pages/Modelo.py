import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Configura o layout para widescreen
st.set_page_config(page_title="Aplicação Widescreen", layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.markdown('''

# Projeto de Deep Learning para Predição do Ponto de Virada Educacional
---
                
Este projeto de Deep Learning tem como objetivo prever se um aluno atingiu o "Ponto de Virada" em seu desenvolvimento educacional. O dataset contém diversas métricas de desempenho educacional e psicossocial de alunos. Utilizamos redes neurais para resolver essa tarefa de classificação binária.

## Preparação dos Dados

O dataset utilizado neste projeto foi carregado a partir de um arquivo CSV contendo dados anonimizados de alunos e suas respectivas métricas de desempenho. As colunas incluem:

- **PEDRA**: Classificação do aluno com base no valor do INDE.
- **IEG**: Indicador de Engajamento.
- **IPS**: Indicador Psicossocial.
- **IPP**: Indicador Psicopedagógico.
- **IDA**: Indicador de Aprendizagem.
- **IAA**: Indicador de Autoavaliação.
- **IAN**: Indicador de Adequação ao Nível.
- **PONTO_VIRADA**: Variável alvo, indicando se o aluno atingiu ou não o ponto de virada.

Decidimos excluir linhas que continham valores ausentes na coluna alvo, `PONTO_VIRADA`, já que ela é crucial para o treinamento e validação do modelo.

```python
df = df.dropna(subset=['PONTO_VIRADA'])
```

### Transformações de Dados

Antes de treinar o modelo, foram necessárias algumas transformações:

1. **Codificação da variável categórica**: A coluna `PEDRA`, que classifica os alunos em diferentes categorias, foi transformada usando o `LabelEncoder`. Isso converteu os valores categóricos em numéricos.
   
2. **Escalonamento dos dados**: Foi utilizado `StandardScaler` para normalizar as features contínuas, garantindo que elas tenham média 0 e desvio padrão 1. Isso é importante para garantir que o modelo não seja enviesado por variáveis com magnitudes diferentes.

```python
label_encoder = LabelEncoder()
X['PEDRA'] = label_encoder.fit_transform(X['PEDRA'])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

3. **Divisão em conjuntos de treino e teste**: Utilizamos `train_test_split` com uma proporção de 80/20 para separar os dados em conjuntos de treinamento e teste. Usamos `stratify=y` para garantir que a distribuição da variável alvo seja mantida nos dois conjuntos, visto que os dados são desbalanceados.

```python
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=64, stratify=y)
```

4. **Pesos das classes**: Como as classes da variável alvo estão desbalanceadas (mais alunos não atingiram o ponto de virada do que os que atingiram), foi calculado o peso das classes com base na proporção de cada classe, para que o modelo não seja enviesado pela classe com maior volume.

```python
class_weights = class_weight.compute_class_weight(class_weight='balanced', classes=np.unique(y_train), y=y_train)
class_weight_dict = dict(enumerate(class_weights))
```

## Arquitetura do Modelo

Utilizamos um modelo sequencial simples com camadas densas (fully connected) e uma camada de regularização `Dropout` para prevenir overfitting. A ativação `ReLU` foi escolhida para as camadas ocultas, enquanto a ativação `sigmoid` foi utilizada na camada de saída, já que estamos tratando de uma tarefa de classificação binária.

```python
model = Sequential()

model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))  # Camada densa com 64 unidades
model.add(Dropout(0.2))  # Dropout para evitar overfitting

model.add(Dense(1, activation='sigmoid'))  # Camada de saída
```

A função de perda escolhida foi a **binary_crossentropy**, apropriada para classificações binárias, e utilizamos o otimizador **Adam**, conhecido por ser eficiente e rápido. Também incluímos as métricas de **accuracy** e **AUC** (Área sob a Curva ROC) para monitorar o desempenho do modelo.

```python
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy', 'AUC'])
```

## Treinamento do Modelo

O modelo foi treinado por 100 épocas, com batch size de 32, e utilizamos uma divisão de 80/20 para o conjunto de validação. Também incorporamos os pesos das classes calculados anteriormente no treinamento para lidar com o desbalanceamento da variável alvo.

```python
historico = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2, class_weight=class_weight_dict)
```

## Visualização dos Resultados

Para avaliar o desempenho do modelo ao longo do tempo, plotamos gráficos que mostram a evolução da perda, acurácia e AUC tanto no conjunto de treinamento quanto no de validação.

![Gráfico de Performance](https://raw.githubusercontent.com/leandric/DATATHON-FIAP/refs/heads/main/img/grafico_performance.png)

## Avaliação no Conjunto de Teste

Após o treinamento, o modelo foi avaliado no conjunto de teste. Os resultados mostraram uma acurácia de 81.1% e uma AUC de 89.2%, indicando que o modelo é capaz de discriminar bem entre as classes.

```python
test_loss, test_acc, test_auc = model.evaluate(X_test, y_test)
print(f'Test loss: {test_loss}, Test accuracy: {test_acc}, Test AUC: {test_auc}')
```
**Test loss: 0.42, Test accuracy: 0.81, Test AUC: 0.89**

## Considerações Finais

As decisões tomadas ao longo deste projeto, como a normalização dos dados, a atribuição de pesos às classes desbalanceadas e o uso de Dropout para evitar overfitting, foram essenciais para garantir que o modelo tenha bom desempenho e generalize bem para novos dados. A abordagem de usar uma rede neural com uma arquitetura simples e funções de ativação adequadas também contribuiu para a eficiência do processo de aprendizado.

''')


with col2:
    # Título da aplicação
    st.markdown('# Protótipo')
    with st.expander('Aplicação'):
        st.title(''' Simular Ponto de Virada''')
        
        # Carregar o modelo
        with open('modelos/model.pkl', 'rb') as f:
            model = pickle.load(f)

        # Carregar o scaler
        with open('modelos/scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)

        # Carregar o label_encoder
        with open('modelos/label_encoder.pkl', 'rb') as f:
            label_encoder = pickle.load(f)

        # Função para predição
        def fazer_predicao(pedra, ieg, ips, ipp, ida, iaa, ian, model, scaler, label_encoder):
            # Estruturar os dados de entrada
            input_data = np.array([[pedra, ieg, ips, ipp, ida, iaa, ian]])
            
            # Transformar a coluna 'PEDRA' com o LabelEncoder
            input_data[:, 0] = label_encoder.transform(input_data[:, 0])
            
            # Escalar os dados de entrada
            input_data_scaled = scaler.transform(input_data)
            
            # Fazer a predição usando o modelo treinado
            predicao = model.predict(input_data_scaled)
            
            # Retornar o valor da predição
            return "Sim" if predicao[0] > 0.5 else "Não"

        # Interface para o usuário
        pedra = st.selectbox("Selecione o valor de PEDRA", label_encoder.classes_)
        ieg = st.number_input("Insira o valor de IEG", min_value=0.0, max_value=10.0, step=0.1)
        ips = st.number_input("Insira o valor de IPS", min_value=0.0, max_value=10.0, step=0.1)
        ipp = st.number_input("Insira o valor de IPP", min_value=0.0, max_value=10.0, step=0.1)
        ida = st.number_input("Insira o valor de IDA", min_value=0.0, max_value=10.0, step=0.1)
        iaa = st.number_input("Insira o valor de IAA", min_value=0.0, max_value=10.0, step=0.1)
        ian = st.number_input("Insira o valor de IAN", min_value=0.0, max_value=10.0, step=0.1)

        # Botão para fazer a predição
        if st.button("Fazer Predição"):
            resultado = fazer_predicao(pedra, ieg, ips, ipp, ida, iaa, ian, model, scaler, label_encoder)
            st.write(f"Resultado da Predição: {resultado}")

    df = pd.read_csv('https://raw.githubusercontent.com/leandric/DATATHON-FIAP/refs/heads/main/data/base_tratada.csv')

    columns = [
    'NOME',
    'ano',
    #'INDE',
    'PEDRA',    
    'IEG',
    'IPS',
    'IPP',
    'IDA',
    'IAA' ,
    'IAN',
    'PONTO_VIRADA'
    ]
    # Deletar as linhas que têm NaN na coluna 'PONTO_VIRADA'
    df = df.dropna(subset=['PONTO_VIRADA'])
    df = df[columns].copy()
    st.markdown('## Tabela para Teste')
    st.dataframe(df.round(2))