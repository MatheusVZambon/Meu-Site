import streamlit as st

st.sidebar.title('Menu')

def login():
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
ID = st.text_input("Digite seu ID:")
nome = st.text_input("Digite seu nome:")
email = st.text_input("Digite seu e-mail:")
prioridade = st.selectbox("Prioridade: ",("Baixa", "Medio", "Alta", "*Critico*"))
assunto = st.text_input("Assunto: ")
mensagem = st.text_input("Messagem: ")

botao = st.link_button("Enviar", "https://docs.google.com/forms/d/e/1FAIpQLSe0_2DQ533BSUEuWf9haVK7w6oUkMei_kFphG-MKGwvA9_bzQ/formResponse?&submit=Submit?usp=pp_url&entry.69514635="+ID+"&entry.1100048191="+nome+"&entry.8340763="+email+"&entry.398253139="+prioridade+"&entry.618138322="+assunto+"&entry.1550799906="+mensagem+"")
