# MEU PRIMEIRO WEB APP
import streamlit as st

pg = st.navigation([st.Page("page1.py")])
pg.run()

usuario = st.text_input("Digite seu Usuario: ")
senha = st.text_input("Senha: ")

botao = st.button("Enviar")
