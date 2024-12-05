import streamlit as st

with open("style.css") as f:
  st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.html(
  "<div><div style='background-color:white; margin=0; padding: 20px; height: 150px; text-align:center;'><div><img src='https://brasil.campus-party.org/wp-content/uploads/2023/08/Logo_Tectoy.png' style='max-height:120px; padding: 10px;'></div></div><div style='background-color: yellow; text-align:center;height:70px;'><h2 style='font-size: 28px; font-weight: bold; color:black;'>Abertura de Chamado</h2></div></div>"
)

ID = st.text_input("Digite seu ID:")
nome = st.text_input("Digite seu nome:")
email = st.text_input("Digite seu e-mail:")
prioridade = st.selectbox("Prioridade: ",("Baixa", "Medio", "Alta", "*Critico*"))
assunto = st.text_input("Assunto: ")
mensagem = st.text_input("Messagem: ")

botao = st.link_button("Enviar", "https://docs.google.com/forms/d/e/1FAIpQLSe0_2DQ533BSUEuWf9haVK7w6oUkMei_kFphG-MKGwvA9_bzQ/formResponse?&submit=Submit?usp=pp_url&entry.69514635="+ID+"&entry.1100048191="+nome+"&entry.8340763="+email+"&entry.398253139="+prioridade+"&entry.618138322="+assunto+"&entry.1550799906="+mensagem+"")


