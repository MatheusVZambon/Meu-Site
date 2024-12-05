import streamlit as st

@st.dialog("Abri um Chamado")
def vote(item):
    ID = st.text_input("Digite seu ID:")
    nome = st.text_input("Digite seu Nome:")
    senha = st.text_input("Digite sua Senha:")
    if nome == 'admin' and senha == 'admin':
        ID = st.text_input("Digite seu ID:")
        nome = st.text_input("Digite seu nome:")
        email = st.text_input("Digite seu e-mail:")
        prioridade = st.selectbox("Prioridade: ",("Baixa", "Medio", "Alta", "*Critico*"))
        assunto = st.text_input("Assunto: ")
        mensagem = st.text_input("Messagem: ")

        botao = st.link_button("Enviar", "https://docs.google.com/forms/d/e/1FAIpQLSe0_2DQ533BSUEuWf9haVK7w6oUkMei_kFphG-MKGwvA9_bzQ/formResponse?&submit=Submit?usp=pp_url&entry.69514635="+ID+"&entry.1100048191="+nome+"&entry.8340763="+email+"&entry.398253139="+prioridade+"&entry.618138322="+assunto+"&entry.1550799906="+mensagem+"")
   

if "vote" not in st.session_state:
    if st.button("Login"): 
        vote("Login")
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"
