import streamlit as st

def show():
    st.markdown('''
# Tech Challenge: PetroPrice Monitor (Documentação)

---
                
Git: [TECH_CHALLENGE_FASE_4](https://github.com/leandric/TECH_CHALLENGE_FASE_4)




## 1. Introdução
Este projeto tem como objetivo analisar os dados históricos do preço do petróleo, realizar uma análise exploratória dos dados (EDA), desenvolver modelos de Machine Learning para prever o preço do petróleo e criar um dashboard interativo para visualização dos resultados.

## 2. Coleta de Dados
Os dados históricos do preço do petróleo foram coletados do site do [IPEA](http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view). A base de dados contém duas colunas principais: data e preço (em dólares).
Tambem coletamos dados usando yahoo finance para de ativos do mercado do petróleo:
* XLE: Energy Select Sector SPDR Fund
O **Energy Select Sector SPDR Fund (XLE)** é um fundo negociado em bolsa (ETF) que busca fornecer resultados de investimento que, antes das despesas, correspondam geralmente ao desempenho do índice de Energy Select Sector. Este ETF é projetado para representar o setor de energia da S&P 500, incluindo empresas envolvidas na produção e distribuição de petróleo e gás, equipamentos de perfuração e outros serviços de energia.

* CL=F: WTI Crude Oil
O **WTI Crude Oil (CL=F)**, ou Petróleo Bruto West Texas Intermediate, é um tipo de petróleo bruto usado como referência no preço do petróleo. É extraído e negociado principalmente nos Estados Unidos e é conhecido por sua alta qualidade devido ao seu baixo teor de enxofre e densidade relativamente baixa.

* BZ=F: Brent Crude Oil
O **Brent Crude Oil (BZ=F)** é uma referência importante para o preço do petróleo a nível mundial. Extraído principalmente do Mar do Norte, o Brent é utilizado como referência para os preços de cerca de dois terços das negociações globais de petróleo bruto. O Brent é conhecido por sua qualidade ligeiramente inferior ao WTI, mas é mais amplamente utilizado como padrão global de preços.


## 3. Análise Exploratória dos Dados (EDA)
A análise exploratória foi realizada para entender melhor a distribuição dos preços do petróleo, identificar tendências e padrões, e detectar outliers.

|                          | Energy Select Sector SPDR Fund | WTI Crude Oil | Brent Crude Oil | Barril     |
|--------------------------|--------------------------------|---------------|-----------------|------------|
| **Count**                | 6430.000000                    | 5998.000000   | 4210.000000     | 6380.000000|
| **Mean**                 | 57.461869                      | 64.518905     | 78.741886       | 64.578966  |
| **Std**                  | 21.085923                      | 25.282054     | 24.660009       | 30.077153  |
| **Min**                  | 19.799999                      | **-37.630001** | 19.330000       | 9.120000   |
| **25%**                  | 36.150002                      | 45.340000     | 59.325000       | 40.277500  |
| **50%**                  | 60.014999                      | 63.105000     | 77.154999       | 63.110000  |
| **75%**                  | 74.300003                      | 83.255001     | 101.250002      | 84.945000  |
| **Max**                  | 101.290001                     | 145.289993    | 146.080002      | 143.950000 |

### Por que o WTI Crude Oil chegou a ter preço negativo?

O preço negativo do WTI Crude Oil observado nos dados pode ser explicado por um evento histórico ocorrido em abril de 2020. Durante essa época, o mercado de petróleo enfrentou uma situação sem precedentes devido a uma combinação de fatores:

**Queda na Demanda Global:** 
   * A pandemia de COVID-19 levou a uma drástica redução na demanda global por petróleo. Com a maioria dos países impondo lockdowns e restrições de viagens, o consumo de petróleo diminuiu significativamente.

**Excesso de Oferta:** 
   * Ao mesmo tempo, a produção de petróleo não foi ajustada rapidamente para compensar a queda na demanda. Isso levou a um excesso de oferta no mercado.

                
**Capacidade de Armazenamento:** 
   * O excesso de oferta e a queda na demanda levaram ao esgotamento da capacidade de armazenamento. Os locais onde o petróleo poderia ser armazenado ficaram saturados.

                
**Vencimento dos Contratos Futuros:**
   * Os preços negativos ocorreram especificamente para os contratos futuros do WTI Crude Oil com vencimento em maio de 2020. Os traders que mantinham esses contratos eram obrigados a aceitar a entrega física do petróleo. Com a falta de espaço de armazenamento, muitos se viram obrigados a pagar para que outros aceitassem a entrega, resultando em preços negativos.

                
Esses fatores combinados criaram uma situação excepcional onde os preços do petróleo caíram abaixo de zero, algo nunca antes visto na história dos mercados de petróleo.               

## Análise da Série Temporal    
<img src="https://raw.githubusercontent.com/leandric/TECH_CHALLENGE_FASE_4/main/img/serie-temporal.png" alt="série Temporal" width="800"/>


1. **Tendência de Alta de Longo Prazo (1998-2008)**:
   - Os preços dos ativos relacionados ao petróleo mostraram uma tendência de alta consistente de 1998 até 2008. Esta tendência pode estar relacionada ao crescimento econômico global e ao aumento da demanda por petróleo.

2. **Crise Financeira Global (2008-2009)**:
   - Em 2008, há uma queda acentuada nos preços dos ativos, coincidente com a crise financeira global. Esta queda foi resultado de uma contração econômica global, que reduziu a demanda por petróleo.

3. **Recuperação Pós-Crise (2009-2014)**:
   - Após a crise de 2008-2009, os preços dos ativos começaram a se recuperar, atingindo novos picos em torno de 2012-2014. Isso pode estar associado à recuperação econômica global e ao aumento da demanda por petróleo.

4. **Queda dos Preços do Petróleo (2014-2016)**:
   - Entre 2014 e 2016, os preços do petróleo caíram significativamente devido a um excesso de oferta global de petróleo, incluindo o aumento da produção de petróleo de xisto nos Estados Unidos.

5. **Oscilações e Recuperação (2016-2019)**:
   - Após a queda de 2014-2016, os preços dos ativos mostraram oscilações, mas mantiveram uma tendência de recuperação moderada até 2019.

6. **Impacto da Pandemia de COVID-19 (2020)**:
   - Em 2020, há uma queda abrupta e temporária nos preços do petróleo, coincidindo com a pandemia de COVID-19. Isso resultou em uma queda drástica na demanda por petróleo devido a lockdowns globais e restrições de viagens, levando até a preços negativos em contratos futuros de petróleo, como observado no WTI Crude Oil.

7. **Recuperação Pós-Pandemia (2021-2024)**:
   - Após o impacto inicial da pandemia, os preços dos ativos voltaram a subir conforme a demanda por petróleo começou a se recuperar. Esta recuperação é visível na série temporal até 2024.

- **Correlação entre Ativos**:
  - Os preços dos diferentes ativos (Energy Select Sector SPDR Fund, WTI Crude Oil, Brent Crude Oil, e o preço do barril de petróleo Brent) tendem a se mover juntos, indicando alta correlação entre eles. Isso pode ser visto nas tendências e oscilações similares ao longo do tempo.
  
- **Volatilidade**:
  - A volatilidade é evidente em vários períodos, especialmente durante crises econômicas e eventos globais significativos, como a crise financeira de 2008 e a pandemia de COVID-19 em 2020.

- **Resiliência e Recuperação**:
  - O mercado de petróleo mostrou resiliência, com preços se recuperando após quedas significativas. A recuperação pós-crise financeira e pós-pandemia são exemplos notáveis dessa resiliência.

##  Análise de correlação
<img src="https://raw.githubusercontent.com/leandric/TECH_CHALLENGE_FASE_4/main/img/correlacao.png" alt="série Temporal" width="800"/>
                
|                           | Energy Select Sector SPDR Fund | WTI Crude Oil | Brent Crude Oil | Barril     |
|---------------------------|--------------------------------|---------------|-----------------|------------|
| **Energy Select Sector SPDR Fund** | 1.000000                       | 0.778755      | 0.597121        | 0.822582   |
| **WTI Crude Oil**         | 0.778755                       | 1.000000      | 0.973940        | 0.980815   |
| **Brent Crude Oil**       | 0.597121                       | 0.973940      | 1.000000        | 0.996401   |
| **Barril**                | 0.822582                       | 0.980815      | 0.996401        | 1.000000   |

### Análise da Correlação Focada no Barril

1. **Correlação entre Barril e Energy Select Sector SPDR Fund (0.822582)**:
   - **Correlação Positiva Forte**: Uma correlação de 0.82 indica uma relação positiva forte entre o preço do barril de petróleo Brent e o Energy Select Sector SPDR Fund. Isso sugere que, quando o preço do barril aumenta, o preço do fundo de energia também tende a aumentar. Essa relação forte pode ser explicada pelo fato de que empresas dentro do Energy Select Sector SPDR Fund são diretamente afetadas pelos preços do petróleo, que impactam seus custos e receitas.

2. **Correlação entre Barril e WTI Crude Oil (0.980815)**:
   - **Correlação Positiva Muito Forte**: A correlação de 0.98 indica uma relação quase perfeita entre o preço do barril de petróleo Brent e o WTI Crude Oil. Isso significa que os preços dos dois tipos de petróleo tendem a se mover juntos quase exatamente. Essa alta correlação é esperada, dado que ambos são benchmarks globais para preços do petróleo e estão sujeitos a influências semelhantes do mercado global.

3. **Correlação entre Barril e Brent Crude Oil (0.996401)**:
   - **Correlação Positiva Quase Perfeita**: A correlação de 0.996 é praticamente perfeita, o que é intuitivo, pois "barril" refere-se ao preço do Brent Crude Oil. Portanto, qualquer movimento no preço do Brent Crude Oil é refletido diretamente no preço do barril de petróleo Brent. Esta correlação quase perfeita confirma que estamos lidando com dados praticamente idênticos.

                
## Análise de dados ausentes.
                
<img src="https://raw.githubusercontent.com/leandric/TECH_CHALLENGE_FASE_4/main/img/serie1.png" alt="série Temporal" width="800"/>
                <img src="https://raw.githubusercontent.com/leandric/TECH_CHALLENGE_FASE_4/main/img/serie2.png" alt="série Temporal" width="800"/>

**Optamos por considerar os dados de 2014 em diante e por excluir os dados de março de 2020 devido ao início da pandemia, que apresentou um comportamento significativamente atípico.**

<img src="https://raw.githubusercontent.com/leandric/TECH_CHALLENGE_FASE_4/main/img/dadosausentes1.png" alt="série Temporal" width="800"/>
                <img src="https://raw.githubusercontent.com/leandric/TECH_CHALLENGE_FASE_4/main/img/dadosausentes2.png" alt="série Temporal" width="800"/>

## Análise da série temporal      

Decompomos a série temporal e analisamos:
                
<img src="https://raw.githubusercontent.com/leandric/TECH_CHALLENGE_FASE_4/main/img/decomposicao.png" alt="série Temporal" width="800"/>
                
### Teste adfuller
Métado para um teste estatístico com a finalidade de aceitar/recusar a hipótese da série ser estacionária

H0 - Hipótese nula (Não é estacionária) H1 - Hipótese alternativa (a série é estacionária)

Quanto maior o p-value, mais evidencia contra a hipótese nula se tem

Rejeitamos a hipótese nula se o p-value for menor que 0.05, ou seja, estamos trabalhando com um intervalode confiança de 95%

| Teste ADF               | Valor                         |
|-------------------------|-------------------------------|
| **Teste estatístico**   | -2.414008733727529            |
| **P-value**             | 0.13782152087377714           |
| **Valores críticos**    |                               |
| **1%**                  | -3.432919034594598            |
| **5%**                  | -2.862674995236558            |
| **10%**                 | -2.5673742003270332           |

**O valor-p é maior que 0.05 e o teste estatístico é maior que os valores críticos de 1%, 5% e 10%. Portanto, não rejeitamos a hipótese nula (H0) de que a série possui uma raiz unitária, indicando que a série não é estacionária.**


## 4. Criamos 3 modelos e mensuramos o desempenho
                

## SARIMAX e ARIMA
                
Criamos um modelo arima como um benchmark de comparação com os outros modelos:
                
<img src="https://raw.githubusercontent.com/leandric/TECH_CHALLENGE_FASE_4/main/img/arima.png" alt="série Temporal" width="800"/>          

### Divisão da Base de Dados

Nesta etapa, dividimos a base de dados em duas partes: treino e teste. A base de teste consiste nos últimos 30 dias da base completa, enquanto a base de treino abrange o restante dos dados.

### Implementação do GridSearch

Realizamos uma implementação da técnica de GridSearch com os seguintes parâmetros:

| Parâmetro | Valores Possíveis |
|-----------|-------------------|
| p         | 0, 1, 2, 3        |
| d         | 0, 1              |
| q         | 0, 1, 2, 3        |
| P         | 0, 1, 2           |
| D         | 0, 1              |
| Q         | 0, 1, 2           |
| m         | 6 (Sazonalidade)  |

### Processo de Treinamento

O GridSearch envolveu cerca de 576 treinamentos. Selecionamos o melhor conjunto de hiperparâmetros com base na performance na base de treino.

### Previsão e Avaliação

Após selecionar os melhores hiperparâmetros, realizamos a previsão para os próximos 30 dias e comparamos os resultados com os valores da base de teste. A métrica utilizada para avaliar a performance foi o MAPE (Mean Absolute Percentage Error).

### Best SARIMA (Base de Treino)(3, 1, 2)x(0, 0, 0, 6) - MAPE (train):0.0187
1. **Mean Absolute Error (MAE)**: 2.802114
   - **Interpretação**: O MAE representa a média dos erros absolutos entre os valores reais e previstos. Um MAE de aproximadamente 2.8 indica que, em média, as previsões do modelo estão a cerca de 2.8 unidades (no caso, dólares) de diferença do valor real do preço do barril de petróleo.

2. **Mean Squared Error (MSE)**: 12.366249
   - **Interpretação**: O MSE é a média dos quadrados dos erros e penaliza mais os erros maiores. Um MSE de 12.367 sugere que há alguns erros maiores nas previsões do modelo, pois a métrica eleva ao quadrado as diferenças antes de calcular a média.

3. **Root Mean Squared Error (RMSE)**: 3.516568
   - **Interpretação**: O RMSE é a raiz quadrada do MSE e está na mesma unidade dos dados originais. Um RMSE de 3.517 indica que, em média, os erros das previsões estão a cerca de 3.5 unidades do valor real do preço do barril de petróleo. Este valor é um pouco maior que o MAE, reforçando que há alguns erros maiores presentes.

4. **Mean Absolute Percentage Error (MAPE)**: 3.417127%
   - **Interpretação**: O MAPE é a média dos erros percentuais absolutos. Um MAPE de aproximadamente 3.42% significa que, em média, a previsão do modelo é 3.42% diferente do valor real. Este é um valor relativamente baixo, indicando que o modelo é bastante preciso em termos percentuais.

5. **R-squared (R²)**: -0.004183
   - **Interpretação**: O R² é o coeficiente de determinação e mede a proporção da variância na variável dependente que é previsível a partir das variáveis independentes. Um valor de R² negativo, como -0.004, sugere que o modelo está se ajustando pior do que uma média simples dos valores reais (ou seja, uma linha horizontal ao longo da média dos valores reais). Isso é um sinal de que o modelo não está capturando bem a relação subjacente nos dados.

Essa análise sugere que, embora o modelo SARIMAX esteja fornecendo previsões relativamente precisas em termos de erro absoluto e percentual, ele pode não estar capturando toda a variabilidade dos dados, como indicado pelo valor negativo de R².               

  
                



## Modelo fbprophet

Tambem usando a tecnica de gridsearch com os seguintes parametros:
                

| Hiperparâmetro              | Valores                         |
|-----------------------------|---------------------------------|
| **Seasonality Mode**        | `additive`, `multiplicative`    |
| **Changepoint Prior Scale** | `0.01`, `0.1`, `0.5`            |
| **Seasonality Prior Scale** | `0.01`, `0.1`, `1.0`            |
                
                
### Melhores Hiperparâmetros
- **Seasonality Mode:** `additive`
- **Changepoint Prior Scale:** `0.01`
- **Seasonality Prior Scale:** `0.01`

### Métricas de Desempenho
| Métrica                      | Valor                          |
|------------------------------|--------------------------------|
| **Mean Absolute Error (MAE)**| `3.2027255410226325`           |
| **Root Mean Squared Error (RMSE)** | `3.634565614514504`      |
| **R² (Coeficiente de Determinação)** | `-0.0727038584038533`  |

<img src="https://raw.githubusercontent.com/leandric/TECH_CHALLENGE_FASE_4/main/img/prophet.png" alt="série Temporal" width="800"/>

                
## 5. Conclusão

O projeto PetroPrice Monitor foi uma iniciativa abrangente que abrangeu desde a coleta e análise de dados históricos de preços de petróleo até o desenvolvimento de modelos preditivos e a criação de um dashboard interativo. A coleta de dados de fontes confiáveis como o IPEA e Yahoo Finance garantiu a robustez das análises subsequentes. A análise exploratória de dados revelou importantes tendências históricas e correlações entre diferentes ativos relacionados ao petróleo, fornecendo um contexto valioso para a modelagem preditiva.

A modelagem preditiva envolveu a implementação e comparação de três diferentes abordagens: SARIMAX, ARIMA e FBProphet, cada uma otimizada através de técnicas de GridSearch para encontrar os melhores hiperparâmetros. O modelo SARIMAX mostrou-se promissor com um MAPE de 3.42%, indicando uma previsão relativamente precisa. No entanto, o valor negativo do R² sugere que o modelo pode não capturar toda a variabilidade dos dados, o que foi uma característica compartilhada, em maior ou menor grau, pelos outros modelos testados.

### Acurácia dos Modelos

A avaliação da acurácia dos modelos preditivos é crucial para entender sua eficácia em prever os preços do petróleo. O modelo SARIMAX apresentou um MAE de 2.8, indicando que, em média, suas previsões estavam a cerca de 2.8 dólares do valor real. O MAPE de 3.42% reforça a precisão do modelo em termos percentuais. Entretanto, o valor negativo de R² (-0.004) sugere que o modelo não conseguiu explicar suficientemente a variabilidade nos dados, apontando limitações em captar todas as dinâmicas do mercado.

O modelo FBProphet, por outro lado, apresentou um MAE de 3.20 e um RMSE de 3.63, com um R² de -0.073. Apesar de ter um desempenho ligeiramente inferior ao SARIMAX em termos de erro absoluto e percentual, o FBProphet ainda se mostrou útil como uma abordagem complementar. A análise das métricas de desempenho de ambos os modelos indica que, embora precisos em termos de erro médio, há espaço para melhorias, especialmente na captura das variações mais sutis dos preços do petróleo.

Por fim, a criação de um dashboard interativo permitiu a visualização clara e intuitiva dos resultados, facilitando a tomada de decisões informadas. Este projeto não apenas demonstrou a aplicabilidade de técnicas de análise de dados e machine learning na previsão de preços de petróleo, mas também destacou a importância de uma abordagem multidisciplinar, combinando conhecimento técnico com uma compreensão profunda do contexto econômico e do mercado.

                ''', unsafe_allow_html=True)

