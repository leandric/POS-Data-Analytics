import streamlit as st
import pandas as pd
import plotly.express as px




def show():
    st.title('Dashboard')
    df = pd.read_csv(
    'https://raw.githubusercontent.com/leandric/TECH_CHALLENGE_FASE_4/main/data/base_de_precos.csv',
    encoding='latin1',
    delimiter=';',
    skiprows=1,
    parse_dates=['Data'],
    dayfirst=True,
    index_col=0,
    usecols=[0, 1],
    names=['Data', 'Preco_do_Bar'])
    df.columns = ['Preco_do_Bar',]
    df.reset_index(inplace=True)
    df.dropna(inplace=True)
    df['Preco_do_Bar'] = df['Preco_do_Bar'].str.replace(',','.')
    df['Preco_do_Bar'] = df['Preco_do_Bar'].astype(float)

    # Adicionando filtro de intervalo de anos
    df['Ano'] = df['Data'].dt.year
    anos = df['Ano'].unique()
    ano_min = int(df['Ano'].min())
    ano_max = int(df['Ano'].max())
    anos_selecionados = st.slider('Selecione o intervalo de anos', ano_min, ano_max, (ano_min, ano_max))

    # Filtrando os dados pelo intervalo de anos selecionado
    df_filtrado = df[(df['Ano'] >= anos_selecionados[0]) & (df['Ano'] <= anos_selecionados[1])]


    # GRAFICOS +++++++++++++++++++++++++++++++++++++++++++++++++++++
    def criar_grafico_ultimo_dia_mes(df):
        """
        Esta função recebe um DataFrame com colunas 'Data' e 'Preco_do_Bar'
        e retorna um gráfico de linha mostrando o preço do barril de petróleo Brent
        no último dia de cada mês.
        
        Parâmetros:
        df (pandas.DataFrame): DataFrame contendo os dados com colunas 'Data' e 'Preco_do_Bar'
        
        Retorna:
        plotly.graph_objs._figure.Figure: Objeto Figure do Plotly
        """
        df['Data'] = pd.to_datetime(df['Data'])  # Convertendo a coluna 'Data' para datetime
        
        # Converter a coluna 'Preco_do_Bar' para numérico, forçando erros a serem NaN
        df['Preco_do_Bar'] = pd.to_numeric(df['Preco_do_Bar'], errors='coerce')
        
        df.set_index('Data', inplace=True)      # Definindo a coluna 'Data' como índice
        
        # Resample para obter o último valor de cada mês
        df_monthly = df.resample('M').last().reset_index()
        
        # Verificar e limpar dados anômalos
        df_monthly = df_monthly[df_monthly['Preco_do_Bar'] < 1000]  # Exemplo de filtro de valores anômalos
        
        # Criando o gráfico de linha usando Plotly Express
        fig = px.line(df_monthly, x='Data', y='Preco_do_Bar', title='Preço do Barril de Petróleo Brent no Último Dia de Cada Mês')
        fig.update_layout(title_font_size=28)
        return fig

    def calcular_variacoes(df):
        """
        Esta função recebe um DataFrame com colunas 'Data' e 'Preco_do_Bar'
        e retorna uma lista com:
        - Valor mais recente e a variação percentual em relação ao dia anterior
        - Valor de 1 dia atrás e a variação percentual em relação ao valor mais recente
        - Valor de 7 dias atrás e a variação percentual em relação ao valor mais recente
        - Valor de 14 dias atrás e a variação percentual em relação ao valor mais recente
        
        Parâmetros:
        df (pandas.DataFrame): DataFrame contendo os dados com colunas 'Data' e 'Preco_do_Bar'
        
        Retorna:
        list: Lista contendo os valores e variações percentuais
        """
        df['Data'] = pd.to_datetime(df['Data'])  # Convertendo a coluna 'Data' para datetime
        df.set_index('Data', inplace=True)      # Definindo a coluna 'Data' como índice
        
        # Ordenando o DataFrame por data
        df = df.sort_index()
        
        # Valor mais recente
        valor_mais_recente = df['Preco_do_Bar'].iloc[-1]
        
        # Valor de 1 dia atrás
        valor_1_dia_atras = df['Preco_do_Bar'].iloc[-2] if len(df) > 1 else None
        
        # Valor de 7 dias atrás
        valor_7_dias_atras = df['Preco_do_Bar'].iloc[-8] if len(df) > 7 else None
        
        # Valor de 14 dias atrás
        valor_14_dias_atras = df['Preco_do_Bar'].iloc[-15] if len(df) > 14 else None
        
        # Cálculo das variações percentuais
        variacao_dia_anterior = (((valor_1_dia_atras / valor_mais_recente) -1)*100) if valor_1_dia_atras else None
        variacao_1_dia = (((valor_1_dia_atras / valor_mais_recente) -1)) if valor_1_dia_atras else None
        variacao_7_dias = (((valor_7_dias_atras / valor_mais_recente) -1)) if valor_7_dias_atras else None
        variacao_14_dias = (((valor_14_dias_atras / valor_mais_recente) -1)) if valor_14_dias_atras else None
        
        return [
            {'Valor': valor_mais_recente, 'Variacao_percentual': 0},
            {'Valor': valor_1_dia_atras, 'Variacao_percentual': round(variacao_1_dia*100,2)},
            {'Valor': valor_7_dias_atras, 'Variacao_percentual': round(variacao_7_dias*100,2)},
            {'Valor': valor_14_dias_atras, 'Variacao_percentual': round(variacao_14_dias*100,2)}
        ]

    def criar_grafico_variacao_mensal(df):
        """
        Esta função recebe um DataFrame com colunas 'Data' e 'Preco_do_Bar'
        e retorna um gráfico de barras mostrando os meses com maior variação percentual
        no preço do barril de petróleo Brent.
        
        Parâmetros:
        df (pandas.DataFrame): DataFrame contendo os dados com colunas 'Data' e 'Preco_do_Bar'
        
        Retorna:
        plotly.graph_objs._figure.Figure: Objeto Figure do Plotly
        """
        df['Data'] = pd.to_datetime(df['Data'])  # Convertendo a coluna 'Data' para datetime
        df.set_index('Data', inplace=True)      # Definindo a coluna 'Data' como índice
        
        # Resample para obter o último valor de cada mês
        df_monthly = df.resample('M').last().reset_index()
        
        # Calcular a variação percentual mês a mês
        df_monthly['Variação_Percentual'] = df_monthly['Preco_do_Bar'].pct_change() * 100
        
        # Remover o primeiro valor, pois será NaN (não há variação para o primeiro mês)
        df_monthly = df_monthly.dropna()
        
        # Criando o gráfico de barras usando Plotly Express
        fig = px.bar(df_monthly, x='Data', y='Variação_Percentual', 
                    title='Variação Percentual Mensal do Preço do Barril de Petróleo Brent',
                    labels={'Variação_Percentual': 'Variação Percentual (%)', 'Data': 'Mês/Ano'})
        fig.update_layout(title_font_size=28)
        return fig

    def criar_grafico_roda_variacao(df):
        """
        Esta função recebe um DataFrame com colunas 'Data' e 'Preco_do_Bar'
        e retorna um gráfico de rosca mostrando a distribuição das variações percentuais mensais.
        
        Parâmetros:
        df (pandas.DataFrame): DataFrame contendo os dados com colunas 'Data' e 'Preco_do_Bar'
        
        Retorna:
        plotly.graph_objs._figure.Figure: Objeto Figure do Plotly
        """
        # Convertendo a coluna 'Data' para datetime
        df['Data'] = pd.to_datetime(df['Data'])
        df.set_index('Data', inplace=True)  # Definindo a coluna 'Data' como índice
        
        # Resample para obter o último valor de cada mês
        df_monthly = df.resample('M').last().reset_index()
        
        # Calcular a variação percentual mês a mês
        df_monthly['Variação_Percentual'] = df_monthly['Preco_do_Bar'].pct_change() * 100
        
        # Remover o primeiro valor, pois será NaN (não há variação para o primeiro mês)
        df_monthly = df_monthly.dropna()
        
        # Agrupar variações percentuais em categorias
        bins = [-float('inf'), -10, -5, 0, 5, 10, float('inf')]
        labels = ['<-10%', '-10% a -5%', '-5% a 0%', '0% a 5%', '5% a 10%', '>10%']
        df_monthly['Categoria'] = pd.cut(df_monthly['Variação_Percentual'], bins=bins, labels=labels)
        
        # Contar a frequência de cada categoria
        categoria_counts = df_monthly['Categoria'].value_counts().reset_index()
        categoria_counts.columns = ['Categoria', 'Frequência']
        
        # Criando o gráfico de rosca usando Plotly Express
        fig = px.pie(categoria_counts, values='Frequência', names='Categoria', hole=0.4, 
                    title='Distribuição das Variações Percentuais Mensais')
        fig.update_layout(title_font_size=28)
        return fig


    # LAYOUT ++++++++++++++++++++++++++++++++++++++++++++++++++++++
    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(criar_grafico_ultimo_dia_mes(df_filtrado.copy()))
        st.markdown('''
        ### Descriçao do Gráfico Variação Percentual Mensal do Preço do Barril de Petróleo Brent
                    
        O gráfico apresenta a variação no preço do barril de petróleo considerando o período selecionado.
        Durante a pandemia de COVID-19, os preços do petróleo passaram por aumentos e quedas significativas. Inicialmente, houve uma queda acentuada devido à redução na demanda global por energia, conforme as restrições de viagem e lockdowns foram implementados ao redor do mundo. Isso resultou em uma queda abrupta na atividade econômica e na demanda por petróleo.

        Conforme alguns países começaram a relaxar as restrições e a demanda por energia começou a se recuperar em certos setores, os preços do petróleo também mostraram recuperações parciais. No entanto, essas flutuações foram marcadas por uma volatilidade incomum, refletindo a incerteza econômica global e as mudanças nas políticas de saúde pública.

        Esses altos e baixos durante a pandemia destacam a sensibilidade do mercado de petróleo às condições econômicas globais e às medidas de resposta à saúde pública, ilustrando a importância de uma análise contínua e detalhada da variação dos preços ao longo do tempo.
        ''')
        st.markdown('<br>', unsafe_allow_html=True)
        st.markdown('<br>', unsafe_allow_html=True)
        st.markdown('<br>', unsafe_allow_html=True)
        st.markdown('''
        ### Descrição do Gráfico de Rosca
        O gráfico de rosca (donut chart) mostra a distribuição das variações percentuais mensais no preço do barril de petróleo Brent ao longo do período analisado. Cada seção do gráfico representa uma categoria de variação percentual, com a área proporcional à frequência de ocorrências dessa variação. As categorias são:
        - **<-10%**: Meses com uma diminuição superior a 10% no preço.
        - **-10% a -5%**: Meses com uma diminuição entre 5% e 10%.
        - **-5% a 0%**: Meses com uma diminuição entre 0% e 5%.
        - **0% a 5%**: Meses com um aumento entre 0% e 5%.
        - **5% a 10%**: Meses com um aumento entre 5% e 10%.
        - **>10%**: Meses com um aumento superior a 10%.

        Este gráfico permite visualizar rapidamente quais faixas de variação foram mais comuns, facilitando a identificação de tendências e padrões no comportamento do preço do petróleo ao longo do tempo.
        ''')
        

    with col2:
        dados = calcular_variacoes(df_filtrado.copy())
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Valor Atual", f"{dados[0]['Valor']}", f"{dados[0]['Variacao_percentual']}%")
        col2.metric("Valor D-1", f"{dados[1]['Valor']}", f"{dados[1]['Variacao_percentual']}%")
        col3.metric("valor D-7", f"{dados[2]['Valor']}", f"{dados[2]['Variacao_percentual']}%")
        col4.metric('Valor D-14',f"{dados[3]['Valor']}",f"{dados[3]['Variacao_percentual']}%")
        st.markdown("""
            ### Descritivo
            
            O gráfico à esquerda demonstra a curva histórica do valor do barril, permitindo a avaliação das sazonalidades e do comportamento ao longo do tempo.
            
            Acima, temos o comparativo dos dias, considerando o valor mais recente do ano escolhido, com os valores do dia anterior, de 7 dias antes e de 14 dias antes dessa data. Dessa forma, temos um comparativo justo da curva e das variações com os mesmos dias da semana.
            """)
        st.markdown('<br>', unsafe_allow_html=True)
        st.markdown('<br>', unsafe_allow_html=True)
        st.markdown('<br>', unsafe_allow_html=True)
        st.markdown('<br>', unsafe_allow_html=True)
        st.markdown('<br>', unsafe_allow_html=True)
        st.plotly_chart(criar_grafico_variacao_mensal(df_filtrado.copy()))
        st.plotly_chart(criar_grafico_roda_variacao(df_filtrado.copy()))
    
    
    st.divider()
