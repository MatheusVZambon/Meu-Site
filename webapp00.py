import streamlit as st

form = st.form("formHD")
usuario = st.text_input("Digite seu Usuario: ")
senha = st.text_input("Senha: ")

botao = st.button("Logar")

pg = st.Page('page1.py')
pg.run()

