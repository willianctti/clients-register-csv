import streamlit as st

st.title("Cadastro de Clientes")

with open("base_dados.csv", "a") as arquivo:
    nome = st.text_input("Digite seu nome: ")
    email = st.text_input("Digite seu email: ")
    data_nascimento = st.date_input("Digite sua data de nascimento: ")
    arquivo.write(f"{nome}\n")

cadastrar = st.button("Cadastrar")

if cadastrar:
    print("Dados salvos com sucesso!") 
    with open("clientes.csv", "a") as arquivo:
        arquivo.write(f"{nome}\n")
        arquivo.write(f"{email}\n")
        arquivo.write(f"{data_nascimento}\n")
