import streamlit as st
import urllib.parse

st.set_page_config(layout="wide")
# Custom HTML/CSS for the banner
custom_html = """

<div id="rodape" align="left">
    <div align="left">
        <h1/>
        <img src="https://assets.folhavitoria.com.br/images/a0322d70-1f5c-11ef-9ec9-9f1d3c6a39fe--minified.jpg" height="300" width="1350"/> 
    </div>
</div>
body {
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    background-color: plum;
}
#rodape {
    width: 100%;
    position: absolute;
    bottom: 0;
    left: 0;
}
#rodape img {
    width: 100%;
    height: 100px;
    position: absolute;
    bottom: 0;
    left: 0;
    object-fit: cover; /* classe pra deixa a imagem com a proporção correta e não ficar achatada */
}
<div class="banner">
    <img src="https://assets.folhavitoria.com.br/images/a0322d70-1f5c-11ef-9ec9-9f1d3c6a39fe--minified.jpg" alt="Banner Image">
</div>
<style>
    .banner {
       width: 160%;
        height: 200px;
        overflow: hidden;
    }
    .banner img {
        width: 100%;
        object-fit: cover;
    }
</style>
"""

# Display the custom HTML
st.components.v1.html(custom_html)

# Função de login
def login_page():
    ID = st.text_input("Digite seu ID:")
    nome = st.text_input("Digite seu nome:")
    senha = st.text_input("Digite sua senha:", type="password")

    if st.button("Login"):
        if nome == 'admin' and senha == 'admin':  # Simples verificação de login
            st.session_state.logged_in = True
            st.session_state.page = "form"  # Redireciona para o formulário após login
            st.success("Login bem-sucedido!")
        else:
            st.error("Nome de usuário ou senha incorretos.")

# Função para o formulário
def form_page():
    ID = st.text_input("Digite seu ID:")
    nome = st.text_input("Digite seu nome:")
    email = st.text_input("Digite seu e-mail:")
    prioridade = st.selectbox("Prioridade: ", ("Baixa", "Média", "Alta", "Crítico"))
    assunto = st.text_input("Assunto: ")
    mensagem = st.text_input("Mensagem: ")

    # Criando o link para o Google Forms com os dados
    base_url = "https://docs.google.com/forms/d/e/1FAIpQLSe0_2DQ533BSUEuWf9haVK7w6oUkMei_kFphG-MKGwvA9_bzQ/formResponse?"
    params = {
        "entry.69514635": ID,
        "entry.1100048191": nome,
        "entry.8340763": email,
        "entry.398253139": prioridade,
        "entry.618138322": assunto,
        "entry.1550799906": mensagem
    }

    # Codificando os parâmetros para a URL
    url = base_url + urllib.parse.urlencode(params)

    # Botão de envio para o Google Forms
    if st.button("Enviar"):
        st.write("Formulário enviado com sucesso!")
        # Redirecionar para o Google Forms com os dados preenchidos
        st.markdown(f'<a href="{url}" target="_blank">Clique aqui para enviar seus dados</a>', unsafe_allow_html=True)

# Verifica se o usuário está logado e decide qual página exibir
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    login_page()  # Exibe a página de login se o usuário não estiver logado
else:
    form_page()  # Exibe o formulário se o usuário estiver logado
