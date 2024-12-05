import streamlit as st

@st.dialog("Abri um Chamado")
def vote(item):
    ID = st.text_input("Digite seu ID:")
    nome = st.text_input("Digite seu Nome:")
    senha = st.text_input("Digite sua Senha:")
    if nome == 'admin' and senha == 'admin':
        st.page_link("page1.py")
    
if "vote" not in st.session_state:
    if st.button("Login"): 
        vote("Login")
