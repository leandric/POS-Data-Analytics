import streamlit as st
import paginas.dashboard as dashboard
import paginas.introducao as introducao
import paginas.modelo as modelo
import paginas.sobre as sobre

st.set_page_config(
    page_title="Tech Challenge",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Definindo os nomes das páginas
page_names_to_funcs = {
    "Documentação": introducao.show,
    "Dashboard": dashboard.show,
    "Modelo": modelo.show,
    "Sobre": sobre.show
}

st.sidebar.title("Navegação")
selected_page = st.sidebar.selectbox("Selecione a página", page_names_to_funcs.keys())

# Executa a função correspondente à página selecionada
page_names_to_funcs[selected_page]()
