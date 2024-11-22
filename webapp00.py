# MEU PRIMEIRO WEB APP
import streamlit as st

form = st.form("formHD")
usuario = st.text_input("Digite seu Usuario: ")
senha = st.text_input("Senha: ")

botao = st.button("Enviar")

if usuario == 'admin' and senha == 'admin':
  StreamlitPage("page1.py")
  StreamlitPage()
