# Tech Challenge - Fase II
## Análise de Séries Temporais com SARIMAX, Prophet e LSTM
Autores:<br>
Leandro Soares da Silva (RM: 352511)<br>
Marcos Barbosa da Silva (RM: 352571)

**Descrição:<br>**
Este projeto analisa a série temporal do índice Ibovespa (BOVA11.SA) utilizando os modelos SARIMAX, Prophet e LSTM. Foram utilizadas técnicas de grid search e análise exploratória para identificar o melhor modelo para a previsão do índice.

**Dados:<br>**
Os dados foram obtidos do Yahoo Finance através da biblioteca yfinance.

**Modelos Utilizados:<br>**
* **SARIMAX** (Seasonal Autoregressive Integrated Moving Average com variáveis exógenas) é uma técnica de modelagem estatística para prever séries temporais, incorporando sazonalidade, tendência e variáveis exógenas, como dados econômicos ou climáticos, para melhorar a precisão das previsões.


* **LSTM** (Long Short-Term Memory) é uma arquitetura de rede neural recorrente usada para previsão de séries temporais, capturando dependências de longo prazo e padrões complexos nos dados.

* **Prophet** é uma biblioteca de previsão de séries temporais desenvolvida pelo Facebook, projetada para modelar dados com sazonalidade, feriados e tendências. É fácil de usar e eficaz, especialmente para conjuntos de dados comuns, fornecendo intervalos de confiança e diagnósticos úteis.

**Metodologia:**<br>

Análise exploratória:
* Visualização da série temporal;<br>
* Cálculo de estatísticas descritivas;<br>
* Identificação de sazonalidade e tendências.<br>

Treinamento e avaliação dos modelos:<br>
* Divisão da série temporal em conjuntos de treino e teste;<br>
* Treinamento dos modelos com diferentes parâmetros;<br>
* Avaliação dos modelos com base em métricas de erro.<br>

Seleção do melhor modelo:<br>
* Seleção do modelo com o menor erro no conjunto de teste;<br>
* Realização de testes adicionais para confirmar a performance do modelo.<br>

**Resultados:<br>**
O modelo SARIMAX apresentou o menor erro no conjunto de teste.
O modelo LSTM foi o segundo melhor modelo.
O modelo Prophet apresentou o maior erro.

### Conclusão:
Com o intuito de enfrentar o desafio proposto, importamos as bibliotecas necessárias para visualização e tratamento de dados. Realizamos a extração dos dados solicitados, considerando o valor de fechamento da Bovespa, utilizando a biblioteca "yfinance". O período abrangido foi de 2018 a 2024, visando obter uma base abrangente de registros, que inclui dados da pandemia de 2019.

Durante a análise exploratória, observamos uma significativa variação nos valores durante o período da pandemia, o que era esperado dadas as circunstâncias. Além disso, identificamos padrões sazonais, embora uma análise mais detalhada em intervalos menores possa fornecer insights adicionais. A tendência clara da série foi confirmada através do teste de AdFuller, mesmo não rejeitando a hipótese nula.

No que diz respeito aos modelos construídos, optamos por SARIMAX, Prophet e LSTM, aplicando técnicas aprendidas durante o curso. O SARIMAX apresentou o menor MAPE, sugerindo uma boa capacidade de previsão. No entanto, reconhecemos a necessidade de realizar mais testes para avaliar sua robustez em prever dados futuros.

O modelo Prophet, apesar de um MAPE variando entre 13% e 7%, mostrou-se mais seguro devido à validação cruzada realizada e à compreensão do intervalo de variação do MAPE. Isso sugere que o modelo pode ser mais confiável em diferentes contextos e períodos.

Por fim, o LSTM, embora tenha exigido normalização dos dados e tenha obtido um MAPE próximo ao do SARIMAX, pode ser explorado mais profundamente em futuros estudos para avaliar seu desempenho em diferentes configurações e períodos.

Concluímos que, embora o SARIMAX tenha sido o destaque em termos de desempenho inicial, o modelo Prophet parece ser a escolha mais segura devido à sua capacidade de generalização e estabilidade, conforme demonstrado pela validação cruzada. No entanto, recomenda-se realizar mais testes e refinamentos em todos os modelos para uma compreensão mais completa de seu desempenho e capacidade de previsão em cenários futuros.

### Requisitos:
```
Python >= 3.7
Poetry
Bibliotecas:
yfinance
pandas
statsmodels
prophet
tensorflow

```
**Como executar:**
Clone o repositório.
Instale as dependências com Poetry: poetry install
Execute o arquivo main.ipynb.
Observações:

*Este projeto é um trabalho acadêmico e não deve ser utilizado para fins de investimento.
Os resultados podem variar de acordo com a série temporal utilizada.*