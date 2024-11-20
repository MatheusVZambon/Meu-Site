# MEU PRIMEIRO WEB APP
import streamlit as st
from ACTlib01 import *
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQFwxxM13bxUC0dpyd0w0PxfZIrJ-hp4Px-R6rsTiG3c3n-89JApzA0jYJpU9vNfxeNCvtJ0Cg35KtO/pub?gid=556192647&single=true&output=csv"
db = Ler_GooglePlanilha(url)
db.fillna('', inplace=True)
Escrever(db)


form = st.form("formHD")
nome = st.text_input("Digite seu nome:")
problema = st.selectbox("Qual o problema apresentado?",("Sem conexão", "Não liga"))
equipamento = st.selectbox("Qual o equipamento com defeito?",("Mouse", "Computador","Monitor","Teclado","Impressora"))
botao = st.button("Enviar")
