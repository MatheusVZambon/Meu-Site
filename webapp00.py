import streamlit as st

ID = st.text_input("Digite seu ID:")
nome = st.text_input("Digite seu Nome:")
senha = st.text_input("Digite sua Senha:")
botao = st.button('Enviar')
    if nome == 'admin' and senha == 'admin':
        st.page_link("page1.py")
    
