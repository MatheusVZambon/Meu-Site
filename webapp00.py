import streamlit as st

def page_2():
    st.title("Page 1")

pg = st.navigation([st.Page("webapp00.py")])
pg.run()

form = st.form("formHD")
usuario = st.text_input("Digite seu Usuario: ")
senha = st.text_input("Senha: ")

botao = st.button("Logar")

if usuario == 'admin' and senha == 'admin':
  pg = st.navigation([st.Page("page1.py")])
  pg.run()
