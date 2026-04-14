import streamlit as st

st.title("🏢 Analisador de Propostas Imobiliárias")

pdf = st.file_uploader("Envie um PDF", type="pdf")

if pdf:
    st.success("PDF carregado com sucesso!")
