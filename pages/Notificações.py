import streamlit as st

st.set_page_config(

    page_title = "Bibliotech",
    page_icon = "📚",
    layout = "wide"



)

st.title("Bibliotech")
st.write("Onde cada página conta uma história.")


st.title("Avisos de Devolução")

# Verifica se existe aviso no session_state
aviso = st.session_state.get("aviso_devolucao", None)

if aviso:
    st.warning(
        f"📚 O livro **{aviso['livro']}** deve ser devolvido até **{aviso['data']}**!"
    )
else:
    st.info("Nenhum aviso de devolução no momento.")


st.markdown("---")
st.write("Credits by Maurício, Otávio, Vitor Emanuel")
