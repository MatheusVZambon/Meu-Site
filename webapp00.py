import streamlit as st

col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)



ID = st.text_input("Digite seu ID:")
nome = st.text_input("Digite seu nome:")
email = st.text_input("Digite seu e-mail:")
prioridade = st.selectbox("Prioridade: ",("Baixa", "Medio", "Alta", "*Critico*"))
assunto = st.text_input("Assunto: ")
mensagem = st.text_input("Messagem: ")

botao = st.link_button("Enviar", "https://docs.google.com/forms/d/e/1FAIpQLSe0_2DQ533BSUEuWf9haVK7w6oUkMei_kFphG-MKGwvA9_bzQ/formResponse?&submit=Submit?usp=pp_url&entry.69514635="+ID+"&entry.1100048191="+nome+"&entry.8340763="+email+"&entry.398253139="+prioridade+"&entry.618138322="+assunto+"&entry.1550799906="+mensagem+"")


# This code example demonstrates how to read colored QR code with color background in Python.
#import aspose.barcode as barcode

# Load QR code image
#reader = barcode.barcoderecognition.BarCodeReader("C:\\Files\\Sample_qr.jpg")

# Specify quality settings to complex background
#reader.quality_settings.allow_complex_background = True    

# Read QR codes
#recognized_results = reader.read_bar_codes()

# Show results
#for x in recognized_results:
    #print("Code Text: " + x.code_text)
    #print("Type: " + x.code_type_name)
