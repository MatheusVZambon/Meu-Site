# MEU PRIMEIRO WEB APP
import streamlit as st

form = st.form("formHD")
ID = st.text_input("Digite seu ID:")
nome = st.text_input("Digite seu nome:")
email = st.text_input("Digite seu e-mail:")
prioridade = st.selectbox("Prioridade: ",("Baixa", "Medio", "Alta", "*Critico*"))
assunto = st.text_input("Assunto: ")
mensagem = st.text_input("Messagem: ")
arquivos = st.file_uploader('Uploader de Arquivo')

#problema = st.selectbox("Qual o problema apresentado?",("Sem Internet", "Alteração de Senha", "Outros"))
botao = st.form_submit_button(label="https://docs.google.com/forms/u/0/d/e/1FAIpQLSe0_2DQ533BSUEuWf9haVK7w6oUkMei_kFphG-MKGwvA9_bzQ/formResponse")
