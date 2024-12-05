import streamlit as st

import streamlit as st

left, middle = st.columns(2, vertical_alignment="bottom")


ID = left.text_input("Digite seu ID:")
nome = left.text_input("Digite seu Nome:")
senha = left.text_input("Digite seu Senha:")

botao = left.button("Enviar")

st.page1(
    page_title="Hello",
    page_icon="👋",
)
