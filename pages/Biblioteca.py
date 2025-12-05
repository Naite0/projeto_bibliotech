import streamlit as st

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

# Inicialização do session_state com a lista de livros se ainda não estiver definida
if "livros" not in st.session_state:
    st.session_state.livros = livros_iniciais

# Função para exibir detalhes do livro
def exibir_detalhes_livro(livro):
    st.write(f"**Nome:** {livro['Nome']}")
    st.write(f"**Autor:** {livro['Autor']}")
    st.write(f"**Ano de Publicação:** {livro['Ano']}")
    st.write(f"**Preço para Aluguel:** R${livro['Preço']:.2f}")

    # Buscar o livro atual no session_state para garantir que a disponibilidade seja persistida
    livro_atual = next((l for l in st.session_state.livros if l['Nome'] == livro['Nome']), None)

    if livro_atual and livro_atual['Disponibilidade']:
        st.write("**Disponibilidade:** Disponível para aluguel!")
        if st.button(f"Alugar '{livro['Nome']}'"):
            # Pergunta de confirmação
            confirmar = st.radio(f"Você tem certeza que deseja alugar '{livro['Nome']}'?", ["Sim", "Não"])

            if confirmar == "Sim":
                livro_atual['Disponibilidade'] = False  # Marca o livro como alugado
                st.success(f"Você alugou '{livro['Nome']}' com sucesso!")
            elif confirmar == "Não":
                st.info("Você decidiu não alugar o livro.")
    else:
        st.write("**Disponibilidade:** Indisponível no momento.")

# Função principal para a aplicação
def app():
    st.header("Escolha um livro para alugar")

    # Exibir todos os livros diretamente sem a necessidade de um botão extra
    for livro in st.session_state.livros:
        exibir_detalhes_livro(livro)

if __name__ == "__main__":
    app()

# Créditos
st.markdown("---")
st.write("Credits by Maurício, Otávio, Vitor Emanuel")
