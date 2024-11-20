# MEU PRIMEIRO WEB APP
import streamlit as st

form = st.form("formHD")
nome = st.text_input("Digite seu nome:")
problema = st.text_input("Qual o problema apresentado?")
#equipamento = st.selectbox("Qual o equipamento com defeito?",("Mouse", "Computador","Monitor","Teclado","Impressora"))
botao = st.button("Enviar")
