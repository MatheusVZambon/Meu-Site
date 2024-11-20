# MEU PRIMEIRO WEB APP
import streamlit as st

form = st.form("formHD")
nome = st.text_input("Digite seu nome:")
email = st.text_input("Digite seu e-mail:")
prioridade = st.selectbox("Baixa", "Medio", "Alta", "*Critico*")

problema = st.selectbox("Qual o problema apresentado?",("Sem Internet", "Alteração de Senha", "Outros"))
botao = st.button("Enviar")
