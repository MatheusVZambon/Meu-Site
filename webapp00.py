import streamlit as st
import aspose.barcode as barcode


ID = st.text_input("Digite seu ID:")
nome = st.text_input("Digite seu nome:")
email = st.text_input("Digite seu e-mail:")
prioridade = st.selectbox("Prioridade: ",("Baixa", "Medio", "Alta", "*Critico*"))
assunto = st.text_input("Assunto: ")
mensagem = st.text_input("Messagem: ")

botao = st.link_button("Enviar", "https://docs.google.com/forms/d/e/1FAIpQLSe0_2DQ533BSUEuWf9haVK7w6oUkMei_kFphG-MKGwvA9_bzQ/formResponse?&submit=Submit?usp=pp_url&entry.69514635="+ID+"&entry.1100048191="+nome+"&entry.8340763="+email+"&entry.398253139="+prioridade+"&entry.618138322="+assunto+"&entry.1550799906="+mensagem+"")

reader = barcode.barcoderecognition.BarCodeReader("https://www.google.com/url?sa=i&url=https%3A%2F%2Fpt.wikipedia.org%2Fwiki%2FC%25C3%25B3digo_QR&psig=AOvVaw1FglxS9486JO_AmY7momXV&ust=1732407251569000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCNio64iW8YkDFQAAAAAdAAAAABAE")

reader.quality_settings.allow_complex_background = True  

recognized_results = reader.read_bar_codes()

for x in recognized_results:
   print("Code Text: " + x.code_text)
   print("Type: " + x.code_type_name)
