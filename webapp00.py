import streamlit as st
#import cv2
#import numpy as np
import aspose.barcode as barcode

reader = barcode.barcoderecognition.BarCodeReader("C:\Users\Administrador\Downloads\Sample_QR")
reader.quality_settings.allow_complex_background = True  
recognized_results = reader.read_bar_codes()
for x in recognized_results:
  print("Code Text: " + x.code_text)
  print("Type: " + x.code_type_name)

image = st.camera_input("Show QR code")

if image is not None:
    bytes_data = image.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    detector = cv2.QRCodeDetector()

    data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)

    st.write("Here!")
    st.write(data)










ID = st.text_input("Digite seu ID:")
nome = st.text_input("Digite seu nome:")
email = st.text_input("Digite seu e-mail:")
prioridade = st.selectbox("Prioridade: ",("Baixa", "Medio", "Alta", "*Critico*"))
assunto = st.text_input("Assunto: ")
mensagem = st.text_input("Messagem: ")

botao = st.link_button("Enviar", "https://docs.google.com/forms/d/e/1FAIpQLSe0_2DQ533BSUEuWf9haVK7w6oUkMei_kFphG-MKGwvA9_bzQ/formResponse?&submit=Submit?usp=pp_url&entry.69514635="+ID+"&entry.1100048191="+nome+"&entry.8340763="+email+"&entry.398253139="+prioridade+"&entry.618138322="+assunto+"&entry.1550799906="+mensagem+"")
