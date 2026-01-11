# Análise da Pandemia COVID-19 - Dados de 2020

Este projeto utiliza Python para analisar os dados da pandemia de COVID-19, cobrindo os meses de setembro, outubro e novembro de 2020. A análise é focada em extrair insights sobre a propagação do vírus, os impactos demográficos e a eficácia das intervenções de saúde.

## Processo de ETL (Extração, Transformação e Carga)

### Extração
Os dados foram coletados de uma fonte confiável, incluindo informações detalhadas sobre os testes realizados, resultados e internações, entre outros aspectos relacionados à saúde durante a pandemia.

### Transformação
- **Renomeação de Colunas**: As colunas foram renomeadas de códigos numéricos para nomes descritivos das perguntas, facilitando a compreensão e análises subsequentes.
- **Normalização de Respostas**: Os códigos de respostas foram substituídos por texto legível, o que permite uma interpretação mais direta dos dados.
- **Reestruturação de Dados**: Utilizamos a técnica de `melt` para transformar o dataframe, aumentando o número de linhas e organizando as perguntas e respostas de forma mais analítica. Um índice foi adicionado para manter o controle sobre o número de respostas após a transformação.

### Carga
- **BigQuery**: Uma classe Python foi desenvolvida para carregar o dataframe transformado no Google BigQuery, garantindo que os dados estivessem acessíveis para análises mais complexas e escaláveis.
- **Integração com Google Looker Studio**: Após a carga no BigQuery, os dados foram conectados ao Google Looker Studio para construção visual das análises.

## Visualização e Análise
O Google Looker Studio foi utilizado para criar um dashboard interativo que apresenta:
- Distribuição regional dos casos de COVID-19.
- Análises demográficas detalhadas baseadas em sexo, idade, escolaridade e outros marcadores.
- Tendências mensais em testes, positividade e internações.

## Implicações e Ações Sugeridas
Com base nas análises, várias ações são sugeridas para lidar com a pandemia, incluindo foco em regiões com alta transmissão, políticas de saúde ajustadas às necessidades demográficas específicas e campanhas de educação e prevenção mais eficazes.

## Conclusão
Este projeto demonstra o poder da análise de dados na gestão de crises de saúde pública, oferecendo insights valiosos que podem ajudar a direcionar recursos e esforços de maneira mais eficaz.

---

Para mais informações, visite nosso dashboard interativo ou entre em contato através das issues neste repositório.
https://lookerstudio.google.com/u/0/reporting/99e92d89-3e11-4eb2-83bf-c7b2cf0e84f8/page/YuyzD