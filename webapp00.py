import streamlit as st

import streamlit as st

left, middle, right = st.columns(3, vertical_alignment="bottom")


ID = left.text_input("Digite seu ID:")
nome = left.text_input("Digite seu nome:")
senha = left.text_input("Digite seu e-mail:")

botao = middle.link_button("Enviar", "https://docs.google.com/forms/d/e/1FAIpQLSe0_2DQ533BSUEuWf9haVK7w6oUkMei_kFphG-MKGwvA9_bzQ/formResponse?&submit=Submit?usp=pp_url&entry.69514635="+ID+"&entry.1100048191="+nome+"&entry.8340763="+email+"&entry.398253139="+prioridade+"&entry.618138322="+assunto+"&entry.1550799906="+mensagem+"")
