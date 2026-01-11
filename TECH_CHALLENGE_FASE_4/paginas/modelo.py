import numpy as np
import pandas as pd
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import streamlit as st
import matplotlib.pyplot as plt

def show():
    # Função para ajustar e prever com os melhores hiperparâmetros fornecidos
    def ajustar_prever_melhor_modelo(train, test, intervalo_dias):
        best_params = {'seasonality_mode': 'additive', 'changepoint_prior_scale': 0.01, 'seasonality_prior_scale': 0.01}
        best_model = Prophet(**best_params)
        best_model.fit(train)
        future = best_model.make_future_dataframe(periods=intervalo_dias)
        forecast = best_model.predict(future)

        mae = mean_absolute_error(test['y'], forecast['yhat'][-intervalo_dias:])
        rmse = np.sqrt(mean_squared_error(test['y'], forecast['yhat'][-intervalo_dias:]))
        r2 = r2_score(test['y'], forecast['yhat'][-intervalo_dias:])

        return forecast, mae, rmse, r2, best_model

    # Função para plotar os resultados
    def plotar_resultados(train, test, forecast, intervalo_dias):
        fig, ax = plt.subplots(figsize=(10, 6))

        # Plotar dados de treino
        ax.plot(train['ds'], train['y'], label='Train Data', color='blue')

        # Plotar dados de teste
        ax.plot(test['ds'], test['y'], label='Test Data', color='red')

        # Plotar previsões
        ax.plot(forecast['ds'], forecast['yhat'], label='Forecast', color='green', linestyle='dashed')

        # Adicionar bandas de intervalo de confiança
        ax.fill_between(forecast['ds'].tail(intervalo_dias), 
                        forecast['yhat_lower'].tail(intervalo_dias), 
                        forecast['yhat_upper'].tail(intervalo_dias), 
                        color='gray', alpha=0.2)

        # Adicionar título e legendas
        ax.set_title('Previsão do Preço do Barril de Petróleo Brent', fontsize=24)
        ax.set_xlabel('Date', fontsize=14)
        ax.set_ylabel('Price', fontsize=14)
        ax.legend()

        st.pyplot(fig)

    # Função principal do Streamlit
    def main():
        st.title('Previsão do Preço do Barril de Petróleo Brent')

        # Carregar os dados a partir do link fornecido
        url = "https://raw.githubusercontent.com/leandric/TECH_CHALLENGE_FASE_4/main/data/base_dash.csv"
        df = pd.read_csv(url)
        df['ds'] = pd.to_datetime(df['ds'])
        df['y'] = pd.to_numeric(df['y'])

        # Selecionar o número de dias para prever
        intervalo_dias = st.number_input("Número de dias para prever", min_value=1, value=30)

        # Dividir os dados em treino e teste
        train = df[:-intervalo_dias]
        test = df[-intervalo_dias:]

        # Ajustar o melhor modelo e fazer previsões
        forecast, mae, rmse, r2, best_model = ajustar_prever_melhor_modelo(train, test, intervalo_dias)

        # Mostrar as métricas de avaliação
        st.write(f"Melhores Hiperparâmetros: {str({'seasonality_mode': 'additive', 'changepoint_prior_scale': 0.01, 'seasonality_prior_scale': 0.01})}")
        st.write(f"MAE: {mae}")
        st.write(f"RMSE: {rmse}")
        st.write(f"R²: {r2}")

        # Plotar os resultados
        plotar_resultados(train, test, forecast, intervalo_dias)

        # Plotar os componentes da previsão
        st.write("Componentes da Previsão:")
        fig_componentes = best_model.plot_components(forecast)
        st.pyplot(fig_componentes)

    main()
