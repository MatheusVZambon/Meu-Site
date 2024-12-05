import streamlit as st

import streamlit as st

left, middle = st.columns(2, vertical_alignment="bottom")


ID = left.text_input("Digite seu ID:")
nome = left.text_input("Digite seu nome:")
senha = left.text_input("Digite seu e-mail:")

botao = middle.button("Enviar")
