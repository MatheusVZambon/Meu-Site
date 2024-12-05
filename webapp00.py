import streamlit as st

@st.dialog("Abri um Chamado")
def vote(item):
    ID = st.text_input("Digite seu ID:")
    nome = st.text_input("Digite seu Nome:")
    senha = st.text_input("Digite sua Senha:")


if "vote" not in st.session_state:
    if st.button("Login"): 
        ote("Login")
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"
