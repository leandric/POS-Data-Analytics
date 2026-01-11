import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno
import matplotlib.pyplot as plt


# Configura o layout para widescreen
#st.set_page_config(page_title="Aplicação Widescreen", layout="wide")

df = pd.read_csv('https://raw.githubusercontent.com/leandric/DATATHON-FIAP/refs/heads/main/data/base_tratada.csv')
df_original = pd.read_csv('https://raw.githubusercontent.com/leandric/DATATHON-FIAP/refs/heads/main/data/PEDE_PASSOS_DATASET_FIAP.csv', sep=';')


# Cria as abas
tab1, tab2, tab3, tab4 = st.tabs(["Introdução", "Análise de Dados: Exploração, Gráficos e Descrições", "Conclusões", "Time 2"])

# Conteúdo da Aba 1
with tab1:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('''
            ## Transformando Vidas com a Associação Passos Mágicos
            Imagine um lugar onde crianças e jovens em situação de vulnerabilidade social encontram esperança e oportunidades para brilhar. Desde 1992, a Associação Passos Mágicos, fundada por Michelle Flues e Dimetri Ivanoff, tem sido esse lugar em Embu-Guaçu. O que começou em orfanatos se transformou, ao longo de 30 anos, em uma ampla gama de programas que oferecem educação de qualidade, suporte psicológico e um espaço para o desenvolvimento integral.
                    
            
            Com uma missão voltada para o desenvolvimento integral, a Associação prepara os jovens para serem protagonistas de suas próprias histórias, oferecendo oportunidades que vão além da sala de aula. Entre os programas oferecidos, destacam-se o apadrinhamento de jovens, intercâmbios culturais e eventos sociais, que incentivam a construção de uma comunidade mais empática e solidária. Através de seus valores centrais, como a empatia e o amor ao aprendizado, a ONG busca criar um ambiente onde todos possam desenvolver seu potencial.
            ''')
        st.markdown('''
        ## Sobre o Conjunto de Dados
Este trabalho se baseia no conjunto de dados e métricas utilizados nas pesquisas do PEDE (Pesquisa Extensiva do Desenvolvimento Educacional) realizadas pela ONG Passos Mágicos nos anos de 2020, 2021 e 2023. Os dados foram coletados pela própria ONG, e as métricas foram desenvolvidas por Dario Rodrigues Silva em parceria com a Passos Mágicos. Esses dados são fundamentais para avaliar o impacto das iniciativas da ONG e compreender a eficácia de suas intervenções ao longo do tempo.
    ''')
        

    with col2:
        st.image('https://yt3.googleusercontent.com/ytc/AIdro_kaSHgX8JGIyURw6ag9sMFtLB_QxMcYWiBOU_4ttvgfKQ=s900-c-k-c0x00ffffff-no-rj',
                 width=400)




# Conteúdo da Aba 2
with tab2:
    
    # Cria o gráfico com missingno
    fig, ax = plt.subplots()
    msno.matrix(df_original, ax=ax)  # Gera o gráfico no 'ax'
    ax.set_yticklabels([])

    col1, col2 = st.columns(2)

    with col1:
        st.header("Modelagem e Análise Exploratória de dados")
        st.markdown('''Inicialmente, estudamos o [Dicionário de Dados do Datathon](https://github.com/leandric/DATATHON-FIAP/blob/main/Dicion%C3%A1rio%20Dados%20Datathon.pdf) para compreender melhor a estrutura e os dados disponíveis. Durante essa análise, observamos que a base de dados utiliza a repetição de colunas para cada ano, o que não seria ideal para conduzir análises robustas. Esse layout resulta em um número elevado de dados nulos nas colunas repetidas. Com isso em mente, realizamos uma análise focada na identificação e tratamento desses dados ausentes.''')
        st.markdown('A base de dados apresenta lacunas em diversas áreas, o que é evidenciado pela presença de três blocos distintos no gráfico. Essa característica está alinhada com a estrutura do conjunto de dados, onde colunas equivalentes são repetidas para cada ano. Isso resulta em uma quantidade significativa de valores ausentes em certas colunas, enquanto outras apresentam dados completos.')
    
    with col2:
        st.pyplot(fig)



    st.markdown('''
## Índice de Desenvolvimento Educacional (INDE)

O Índice de Desenvolvimento Educacional (INDE) é composto por uma ponderação de diferentes métricas utilizadas no processo avaliativo dos alunos, abrangendo indicadores como **IAN**, **IDA**, **IEG**, **IAA**, **IPS**, **IPP** e **IPV**. Esses indicadores foram cuidadosamente desenvolvidos para proporcionar uma avaliação ampla e precisa, permitindo que os profissionais identifiquem as áreas em que cada aluno enfrenta maiores dificuldades e oferecendo suporte direcionado.
''')
    st.markdown('''
    Ao analisar o desempenho dos alunos entre **2020 e 2022**, notamos uma variação nas notas, que caíram de **7,3** em 2020 para **6,89** em 2021, mas apresentaram uma recuperação em 2022, com uma média de **7,03**. É fundamental lembrar que 2020 foi um ano atípico, marcado pelos impactos da pandemia, que afetou principalmente os alunos já vulneráveis a fatores sociais. No entanto, a partir de 2021, observa-se uma tendência de recuperação e crescimento nos indicadores, refletindo o esforço contínuo dos profissionais que trabalham diariamente com as crianças, visando à melhoria do desempenho educacional.
    ''')
    # Converter a coluna 'INDE' para valores numéricos (forçando erros para NaN)
    df['INDE'] = pd.to_numeric(df['INDE'], errors='coerce')

    # Remover linhas onde 'INDE' ou 'ano' tenham valores ausentes (NaN)
    df_clean = df.dropna(subset=['INDE', 'ano'])

    # Filtrar para mostrar apenas os anos 2020, 2021 e 2022
    df_filtered = df_clean[df_clean['ano'].isin([2020, 2021, 2022])]

    # Agrupar por 'ano' e calcular a média do INDE
    df_grouped = df_filtered.groupby('ano')['INDE'].mean().reset_index()

    # Criar o gráfico de colunas (barras) usando Matplotlib com cor azul pastel
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(df_grouped['ano'], df_grouped['INDE'], color='#AEC6CF')

    # Adicionar título e rótulos
    ax.set_title('Média do Índice de Desenvolvimento Educacional ao Longo dos Anos (2020-2022)')
    ax.set_xlabel('Ano')

    # Remover os números do eixo Y
    ax.set_yticks([])

    # Adicionar rótulos nas barras
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

    # Ajustar os ticks do eixo X para mostrar apenas os anos 2020, 2021 e 2022
    ax.set_xticks([2020, 2021, 2022])

    # Remover a legenda (caso haja)
    ax.legend().set_visible(False)

    # Mostrar o gráfico no Streamlit
    st.pyplot(fig)    

    st.markdown('''
## Classificação do INDE

O modelo de classificação do INDE categoriza o desempenho dos alunos de acordo com o seu índice, nas seguintes faixas:

- **Quartzo**: 2,405 a 5,506
- **Ágata**: 5,506 a 6,868
- **Ametista**: 6,868 a 8,230
- **Topázio**: 8,230 a 9,294

A crescente valorização da classificação **Ametista** sugere um aumento de estudantes com um perfil mais diferenciado, enquanto a redução na classificação **Ágata** pode indicar uma mudança nas expectativas e no perfil dos alunos ao longo dos anos. Essas alterações podem também estar relacionadas a mudanças nos critérios de avaliação implementados ao longo do tempo, que passaram a reconhecer diferentes aspectos do desempenho dos alunos. Esses padrões podem ser observados nos gráficos e na tabela abaixo.

## Análise das Pedras-Conceito

Entre **2016 e 2022**, a distribuição dos alunos nas categorias de pedras-conceito variou. A **Ágata** foi dominante em anos como 2016 (**47%**) e 2019 (**34%**), mas apresentou queda a partir de 2021 (**21%**) e 2022 (**30%**). Em contrapartida, a **Ametista** cresceu consistentemente, tornando-se a pedra mais atribuída desde 2020, atingindo **50%** em 2021.

Essa mudança pode refletir tanto uma alteração no perfil dos ingressantes quanto ajustes nos critérios de avaliação. A **Topázio** permaneceu estável, indicando pouca mudança no critério de avaliação para essa categoria ao longo dos anos. A análise revela uma adaptação nos métodos de avaliação e um foco maior em características diferenciadas dos alunos.
                
''')

    st.markdown('''![Gráfico de Performance](https://raw.githubusercontent.com/leandric/DATATHON-FIAP/refs/heads/main/img/dados_relatorio.png)
                ![Gráfico de Performance](https://raw.githubusercontent.com/leandric/DATATHON-FIAP/refs/heads/main/img/grafico_162_relatorio.png)
                *Fonte: Pesquisa PEDE 2020*''')
    
    
    st.markdown('''    
## Índice de Engajamento (IEG)

O Índice de Engajamento (IEG) foi um dos principais fatores que contribuíram para a queda no desempenho estudantil em **2021**. Ao comparar as notas desse índice entre **2020** e **2021**, observamos uma redução média de **10,9%** na classificação geral (INDE). Analisando a classificação por categoria, a situação se agravou, com uma queda de **33,9%**.

Diante desse cenário, a entidade decidiu reavaliar e reintegrar o campo "Destaque de Engajamento", que foca na entrega das lições de casa. Ao comparar os anos de **2021** e **2022**, verificamos uma recuperação significativa: o aumento no índice geral foi de **15,2%**. A categoria que mais se destacou foi a **"Quartzo"**, cuja média subiu de **3,06** em 2021 para **5,23** em 2022, representando um impressionante crescimento de **71%**.

Esses resultados ressaltam a importância do engajamento dos alunos e a eficácia das intervenções realizadas para melhorar seu desempenho.                    
                    ''')
    

    # Converter a coluna 'IEG' para valores numéricos (forçando erros para NaN)
    df['IEG'] = pd.to_numeric(df['IEG'], errors='coerce')

    # Remover linhas onde 'IEG' ou 'ano' tenham valores ausentes (NaN)
    df_clean = df.dropna(subset=['IEG', 'ano'])

    # Filtrar para mostrar apenas os anos 2020, 2021 e 2022
    df_filtered = df_clean[df_clean['ano'].isin([2020, 2021, 2022])]

    # Agrupar por 'ano' e calcular a média do IEG
    df_grouped = df_filtered.groupby('ano')['IEG'].mean().reset_index()

    # Criar o gráfico de colunas (barras) usando Matplotlib com cor azul pastel
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(df_grouped['ano'], df_grouped['IEG'], color='#AEC6CF')

    # Adicionar título e rótulos
    ax.set_title('Média do Indicador de Engajamento ao Longo dos Anos (2020-2022)')
    ax.set_xlabel('Ano')

    # Remover os números do eixo Y
    ax.set_yticks([])

    # Adicionar rótulos nas barras
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

    # Ajustar os ticks do eixo X para mostrar apenas os anos 2020, 2021 e 2022
    ax.set_xticks([2020, 2021, 2022])

    # Remover a legenda (caso haja)
    ax.legend().set_visible(False)

    # Mostrar o gráfico no Streamlit
    st.pyplot(fig)

    st.markdown('''
## Destaque no Indicador de Aprendizagem (IDA)

O destaque no **Indicador de Aprendizagem (IDA)** entre os períodos de **2020** e **2021** foi observado nos alunos classificados como **"Quartzo"**, que foram os únicos a apresentar um rendimento superior nesse comparativo. Além disso, no período de **2021** a **2022**, esses alunos registraram um ganho de **40%**. Considerando que o **IDA** é um indicador de aprendizagem continuada, havia uma expectativa de crescimento na última classificação. No entanto, não se previu a queda de **16%** nos alunos classificados como **"Ametista"** e **"Topázio"**.

No contexto geral, o índice apresentou uma queda de **14%** em **2021**, seguida por um crescimento de **11%** em **2022**. Assim, no acumulado, observa-se uma tendência de recuperação para **2023**.
''')
    df['IDA'] = pd.to_numeric(df['IDA'], errors='coerce')

    # Remover linhas onde 'IDA' ou 'ano' tenham valores ausentes (NaN)
    df_clean = df.dropna(subset=['IDA', 'ano'])

    # Filtrar para mostrar apenas os anos 2020, 2021 e 2022
    df_filtered = df_clean[df_clean['ano'].isin([2020, 2021, 2022])]

    # Agrupar por 'ano' e calcular a média do IDA
    df_grouped = df_filtered.groupby('ano')['IDA'].mean().reset_index()

    # Criar o gráfico de colunas (barras) usando Matplotlib com cor azul pastel
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(df_grouped['ano'], df_grouped['IDA'], color='#AEC6CF')

    # Adicionar título e rótulos
    ax.set_title('Média do Indicador de Aprendizagem ao Longo dos Anos (2020-2022)')
    ax.set_xlabel('Ano')

    # Remover os números do eixo Y
    ax.set_yticks([])

    # Adicionar rótulos nas barras
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

    # Ajustar os ticks do eixo X para mostrar apenas os anos 2020, 2021 e 2022
    ax.set_xticks([2020, 2021, 2022])

    # Remover a legenda (caso haja)
    ax.legend().set_visible(False)

    # Mostrar o gráfico no Streamlit
    st.pyplot(fig)

    st.markdown('''
## Oscilação nos Indicadores de Engajamento

O gráfico destaca uma oscilação nos indicadores de engajamento, com o ano de **2021** representando um ponto de recuperação em relação a **2020**, seguido por uma estabilização em **2022**. Esses pontos de virada podem estar associados a fatores externos e internos no ambiente educacional:

## Impacto da Pandemia
A pandemia teve um impacto significativo no engajamento dos estudantes, especialmente em **2020**, quando a maioria das escolas enfrentou desafios técnicos e estruturais para a implementação do ensino remoto.

## Adaptação e Melhoria de Ferramentas Educacionais
Em **2021**, observou-se um crescimento no engajamento, refletindo uma melhor adaptação das escolas, professores e alunos às novas tecnologias educacionais e aos métodos de ensino a distância.

## Readaptação ao Ensino Presencial
Em **2022**, com a reabertura das escolas, o engajamento apresentou uma leve queda, o que pode ser explicado pela readaptação dos estudantes ao ensino presencial, após quase dois anos de ensino remoto, e pelo possível impacto psicológico e emocional da pandemia sobre os alunos.    
''')
    df['IPV'] = pd.to_numeric(df['IPV'], errors='coerce')

    # Remover linhas onde 'IPV' ou 'ano' tenham valores ausentes (NaN)
    df_clean = df.dropna(subset=['IPV', 'ano'])

    # Filtrar para mostrar apenas os anos 2020, 2021 e 2022
    df_filtered = df_clean[df_clean['ano'].isin([2020, 2021, 2022])]

    # Agrupar por 'ano' e calcular a média do IPV
    df_grouped = df_filtered.groupby('ano')['IPV'].mean().reset_index()

    # Criar o gráfico de colunas (barras) usando Matplotlib com cor azul pastel
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(df_grouped['ano'], df_grouped['IPV'], color='#AEC6CF')

    # Adicionar título e rótulos
    ax.set_title('Média do Indicador de Ponto de Virada ao Longo dos Anos (2020-2022)')
    ax.set_xlabel('Ano')

    # Remover os números do eixo Y
    ax.set_yticks([])

    # Adicionar rótulos nas barras
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

    # Ajustar os ticks do eixo X para mostrar apenas os anos 2020, 2021 e 2022
    ax.set_xticks([2020, 2021, 2022])

    # Remover a legenda (caso haja)
    ax.legend().set_visible(False)

    # Mostrar o gráfico no Streamlit
    st.pyplot(fig)

    st.markdown('''
## Matriz de Correlação

Essa matriz ajuda a identificar quais aspectos do engajamento e da aprendizagem têm mais influência sobre o desempenho educacional e os momentos críticos no progresso dos alunos.

## Interpretação das Variáveis

- **IEG (Indicador de Engajamento)**: Reflete o nível de engajamento dos alunos.
- **IPV (Indicador de Ponto de Virada)**: Representa momentos críticos que influenciam o desempenho do aluno.
- **INDE (Índice de Desenvolvimento Educacional)**: Uma métrica global que pondera vários indicadores, incluindo o aprendizado e o engajamento.
- **IDA (Indicador de Aprendizagem)**: Avalia a qualidade da aprendizagem do aluno.

## Análise das Correlações

- **IEG e INDE (0.8)**: A alta correlação sugere que o engajamento dos alunos está fortemente relacionado ao desenvolvimento educacional geral. Ou seja, quanto maior o engajamento, melhor o desempenho no índice geral.
- **IEG e IDA (0.57)**: O engajamento também está positivamente relacionado com a aprendizagem, embora a correlação seja moderada, indicando que outros fatores além do engajamento podem influenciar a aprendizagem.
- **IEG e IPV (0.51)**: Uma correlação moderada entre engajamento e momentos decisivos de desempenho sugere que o engajamento influencia, mas não é o único fator para os pontos de virada no desempenho.
- **IDA e INDE (0.81)**: A aprendizagem está fortemente correlacionada ao desenvolvimento educacional, o que faz sentido, pois a qualidade da aprendizagem é um componente chave desse índice.
- **IDA e IPV (0.35)**: A correlação mais baixa indica que os momentos críticos de desempenho não influenciam tanto a aprendizagem quanto outros fatores.
- **INDE e IPV (0.6)**: A correlação moderada entre o índice de desenvolvimento educacional e os pontos de virada indica que momentos decisivos influenciam o desenvolvimento educacional de forma relevante.
''')
    df_filtered = df[['IEG', 'IDA', 'INDE', 'IPV']].dropna()

    # Calcular a matriz de correlação
    correlation_matrix = df_filtered.corr()

    # Criar o heatmap de correlação usando Seaborn
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='BuPu', vmin=-1, vmax=1, ax=ax)

    # Adicionar título
    ax.set_title('Matriz de Correlação entre IEG, IDA, INDE e IPV')

    # Mostrar o gráfico no Streamlit
    st.pyplot(fig)






# Conteúdo da Aba 3
with tab3:
    st.markdown('''
                # Conclusão
Este trabalho combinou uma análise exploratória de dados e um modelo de Deep Learning para analisar e prever o desempenho educacional dos alunos acompanhados pela *Associação Passos Mágicos*, uma organização dedicada ao desenvolvimento integral de jovens em situação de vulnerabilidade social. A análise dos dados de 2020 a 2022 mostrou os impactos da pandemia sobre o engajamento e aprendizagem, bem como a eficácia das intervenções oferecidas pela ONG. Utilizando redes neurais densas, foi possível prever o "Ponto de Virada" educacional dos alunos com uma acurácia de 81,1% e AUC de 89,2%, evidenciando a importância de variáveis como o Índice de Engajamento (IEG) e o Indicador de Aprendizagem (IDA).

Além disso, este trabalho reforça o papel transformador da *Associação Passos Mágicos*, que, ao longo de 30 anos, tem oferecido suporte educacional e emocional para jovens em Embu-Guaçu. Os dados coletados pela ONG e utilizados neste estudo, provenientes da Pesquisa Extensiva do Desenvolvimento Educacional (PEDE), foram essenciais para avaliar o impacto de suas iniciativas. A análise dos resultados indica que o trabalho da Associação não apenas melhora o desempenho educacional dos alunos, mas também os prepara para serem protagonistas de suas próprias histórias, reafirmando a missão da ONG de transformar vidas por meio da educação e do suporte integral.

''')
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('''
Gostaríamos de parabenizar a Associação Passos Mágicos pela iniciativa, empenho e resiliência dos profissionais que dedicam seus dias a melhorar a vida de quem mais precisa. O trabalho de vocês não só transforma a realidade de crianças em situação de vulnerabilidade social, oferecendo-lhes mais chances na vida, como também melhora a sociedade com essa nobre ação. Que o esforço e a paixão de toda a equipe continuem fazendo a diferença e inspirando todos ao redor!
''')
    with col2:
        st.image('https://yt3.googleusercontent.com/ytc/AIdro_kaSHgX8JGIyURw6ag9sMFtLB_QxMcYWiBOU_4ttvgfKQ=s900-c-k-c0x00ffffff-no-rj',
                 width=400)

# Conteúdo da Aba 4
with tab4:
    def show():
        st.title("Sobre o Time 2")
        st.write("Conheça os membros do nosso time abaixo:")

        # Definindo informações sobre cada membro
        team_members = [{  "name": "Emily da Silva Vaculik",
                "photo": "https://media.licdn.com/dms/image/v2/D4D03AQFS8a2Sq03t6g/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1675709544684?e=1732752000&v=beta&t=RLwf2NJZTPdN-kSNGIuZujV0Yn4OWcIAEWIYSItzVHQ",  
                "graduation": "Engenheira de Alimentos - Faculdade de Tecnologia Termomecanica",
                "description":"Gerente de Contas Externas",
                "linkedin": "https://www.linkedin.com/in/emily-vaculik-9a82ab202/"
            },
            {  "name": " Marcos Barbosa da Silva",
            "photo": "https://media.licdn.com/dms/image/v2/D4D03AQF26Tn_uiB3FQ/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1686167990179?e=1732752000&v=beta&t=EC1FSU5IiAIy_wPxxnP7HEMXZQ_lSZVEVNXPrVbcREc", 
            "graduation": " Administração de Empresas - Faculdade Impacta Tecnologia",
            "description":" Business Intelligence Sr",
            "linkedin": "https://www.linkedin.com/in/marcos-silva-61705b31/"},
            {
                "name": "Leandro Soares da Silva",
                "photo": "https://media.licdn.com/dms/image/v2/D4D03AQEgGiOQOS8Jag/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1724201241884?e=1732752000&v=beta&t=KTga6jt8C9MV0iYlbKRJgLnedn0hG7zAjfvvz1Pdin8",
                "graduation": "Bacharel em Engenharia de Computação",
                "description": "Analista de Dados",
                "linkedin": "https://www.linkedin.com/in/leandro-soares-11b010115/"
            },
        ]

        # Exibindo informações sobre cada membro
        for member in team_members:
            st.subheader(member["name"])
            st.image(member["photo"], width=150)
            st.write(member["description"])
            st.write(f"[LinkedIn]({member['linkedin']})")
            st.markdown("---")
    show()








