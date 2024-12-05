import streamlit as st

st.sidebar.title('Menu')

def page1():
    st.title("Login")
    st.write("Bem-vindo ao nosso aplicativo multipágina!")

def graficos():
    st.title("Gráficos")
    st.write("Aqui você pode ver alguns gráficos.")

def mapas():
    st.title("Mapas")
    st.write("Aqui você pode ver alguns mapas.")

def tabelas():
    st.title("Tabelas de Dados")
    st.write("Aqui você pode ver algumas tabelas de dados.")

# Dicionário de páginas
paginas = {
    "Login": login
}

# Menu de navegação
st.sidebar.title("Navegação")
pagina_selecionada = st.sidebar.selectbox("Selecione uma página", paginas.keys())

# Exibir a página selecionada
paginas[pagina_selecionada]()
