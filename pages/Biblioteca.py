import streamlit as st
import datetime

# Configuração da página
st.set_page_config(
    page_title="Bibliotech",
    page_icon="📚",
    layout="wide"
)

# Título e descrição
st.title("Bibliotech")
st.write("Onde cada página conta uma história.")

# Lista de livros pré-definidos
livros_iniciais = [
    {'Nome': 'O Senhor dos Anéis', 'Autor': 'J.R.R. Tolkien', 'Ano': 1954, 'Preço': 30.0, 'Disponibilidade': True},
    {'Nome': '1984', 'Autor': 'George Orwell', 'Ano': 1949, 'Preço': 25.0, 'Disponibilidade': False},
    {'Nome': 'O Hobbit', 'Autor': 'J.R.R. Tolkien', 'Ano': 1937, 'Preço': 28.0, 'Disponibilidade': True},
    {'Nome': 'Harry Potter e a Pedra Filosofal', 'Autor': 'J.K. Rowling', 'Ano': 1997, 'Preço': 35.0, 'Disponibilidade': True},
    {'Nome': 'Dom Casmurro', 'Autor': 'Machado de Assis', 'Ano': 1899, 'Preço': 20.0, 'Disponibilidade': True}
]

# Inicialização do session_state
if "livros" not in st.session_state:
    st.session_state.livros = livros_iniciais


# Função para exibir detalhes do livro
def exibir_detalhes_livro(livro):

    with st.container():
        st.markdown(
            """
            <div style="
                padding: 15px;
                border: 2px solid #4A90E2;
                border-radius: 10px;
                margin-bottom: 15px;
                background-color: #F5F9FF;">
            """,
            unsafe_allow_html=True
        )

        st.subheader(livro['Nome'])
        st.write(f"**Autor:** {livro['Autor']}")
        st.write(f"**Ano:** {livro['Ano']}")
        st.write(f"**Preço para Aluguel:** R${livro['Preço']:.2f}")

        # Buscar o livro atualizado
        livro_atual = next((l for l in st.session_state.livros if l['Nome'] == livro['Nome']), None)

        # Se disponível
        if livro_atual['Disponibilidade']:

            st.success("Disponível para aluguel ✔")

            # Botão com key ÚNICA
            if st.button(
                f"Alugar '{livro['Nome']}'",
                key=f"btn_alugar_{livro['Nome'].replace(' ', '_')}"
            ):

                confirmar = st.radio(
                    f"Confirmar aluguel de '{livro['Nome']}'?",
                    ["Sim", "Não"],
                    key=f"confirm_{livro['Nome'].replace(' ', '_')}"
                )

                if confirmar == "Sim":
                    livro_atual['Disponibilidade'] = False

                    # Data de devolução
                    data_devolucao = datetime.date.today() + datetime.timedelta(days=7)

                    st.session_state["aviso_devolucao"] = {
                        "livro": livro['Nome'],
                        "data": data_devolucao.strftime("%d/%m/%Y")
                    }

                    st.success(f"📚 Você alugou '{livro['Nome']}'!")
                else:
                    st.info("Aluguel cancelado.")

        # Se indisponível
        else:
            st.error("Indisponível no momento ❌")

        st.markdown("</div>", unsafe_allow_html=True)


# Função principal
def app():
    st.header("Escolha um livro para alugar")

    for livro in st.session_state.livros:
        exibir_detalhes_livro(livro)


if __name__ == "__main__":
    app()

st.markdown("---")
st.write("Credits by Maurício, Otávio, Vitor Emanuel")
