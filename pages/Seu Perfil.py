import streamlit as st
import datetime

st.set_page_config(

    page_title="Bibliotech",
    page_icon="📚",
    layout="wide"
    
)

st.title("Bibliotech")
st.write("Onde cada página conta uma história.")


if "logado" not in st.session_state:
    st.session_state.logado = False

if "usuario" not in st.session_state:
    st.session_state.usuario = ""

if "data_conta" not in st.session_state:
    st.session_state.data_conta = None


if not st.session_state.logado:

    st.header("Login")

    nome = st.text_input("Usuário")
    sen = st.text_input("Senha", type="password")

    if st.button("Fazer Login"):

        if nome != "" and sen != "":
            st.session_state.usuario = nome
            st.session_state.data_conta = datetime.date.today()
            st.session_state.logado = True
            st.success("Login realizado com sucesso!")
        else:
            st.error("Preencha usuário e senha!")


else:
    st.header("Seu Perfil")

    data_formatada = st.session_state.data_conta.strftime("%d/%m/%Y")
    st.write(f"**Usuário:** {st.session_state.usuario}")
    st.write(f"**Conta criada no dia:** {data_formatada}")

    if st.button("Sair"):
        st.session_state.logado = False
        st.session_state.usuario = ""
        st.session_state.data_conta = None
        st.rerun()   

st.markdown("---")
st.write("Credits by Maurício, Otávio, Vitor Emanuel")
