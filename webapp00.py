import streamlit as st

import streamlit as st

left, middle = st.columns(2, vertical_alignment="bottom")


ID = left.text_input("Digite seu ID:")
nome = left.text_input("Digite seu Nome:")
senha = left.text_input("Digite seu Senha:")

botao = left.button("Enviar")

st.page_link("pages/page1.py", label="Page 1", icon="1️⃣")
