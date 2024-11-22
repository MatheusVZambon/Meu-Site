import streamlit as st

usuario = st.text_input("Digite seu Usuario: ")
senha = st.text_input("Senha: ")

botao = st.button("Enviar")
pg = st.navigation([st.Page("webapp00.py")])
pg.run()

