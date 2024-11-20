# MEU PRIMEIRO WEB APP
import streamlit as st

form = st.form("formHD")
ID = st.text_input("Digite seu ID:")
nome = st.text_input("Digite seu nome:")
email = st.text_input("Digite seu e-mail:")
prioridade = st.selectbox("Prioridade: ",("Baixa", "Medio", "Alta", "*Critico*"))
assunto = st.text_input("Assunto: ")
mensagem = st.text_input("Messagem: ")

linhas = arquivo.readlines()
for linha in linhas:
    print(linha)
#problema = st.selectbox("Qual o problema apresentado?",("Sem Internet", "Alteração de Senha", "Outros"))
botao = st.button("Enviar")
