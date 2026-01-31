#passo 1: criar o site e colocar os inputs e botoes
#passo 2: conseguir registrar os eventos
#passo 3: conseguir salvar e visualizar

import pandas as pd
import streamlit as st
import os



st.set_page_config(
    page_title="Convite casamento",
    page_icon="https://cdn-icons-png.flaticon.com/512/531/531813.png"

)

names = "lista.csv"



col1, col2, col3 = st.columns([1,40,1])

with col2.container(key="minha_coluna_estilizada"):
    input_name = st.text_input("Nome", key="nome", placeholder="Digite seu nome")
    input_lastname = st.text_input("Sobrenome", key="sobrenome", placeholder="Digite seu sobrenome")

    st.markdown("<div style='height:200px'></div>", unsafe_allow_html=True)
    
    b1, b2, b3 = st.columns([1,2,1])
    with b2:
        with b2.container(key="messagem"):
            message_confirmar = st.write("Para confirmar a sua presença, preencha os campos a cima e aperte em confirmar.")
            message_cancelar = st.write("Caso queira tirar seu nome da lista, entrar em contato com Andrew ou Lay.")
            with b2:
                aceitar = st.button("Confirmar presença", key="accept_button", use_container_width=True)


st.markdown("""
    <style>
    .st-key-minha_coluna_estilizada {
        background-color: #f7c8e7;
        border: 2px solid #b06d99;
        padding: 30px;
        border-radius: 35px;
        min-height: 420px;
        max-width: 2000px;
        margin: 0 auto;
    }

    .st-key-accept_button button {
        max-width: 300px;  
        margin: 0 auto;    
        background-color: #f059bc;
        color: black;
        font-weight: 600;
        border-radius: 10px;
    }
    .st-key-accept_button button:hover {
        max-width: 300px;  
        margin: 0 auto;    
        background-color: #9e3a7c;
        color: black;
        font-weight: 600;
        border-radius: 10px;
    }
            
    html, body {
        width: 100%;
        min-height: 100%;
        margin: 0;
        padding: 0;
        overflow-x: hidden;

        background-image: url("https://static.vecteezy.com/system/resources/thumbnails/023/402/460/original/watercolor-beautiful-floral-bloom-animation-of-colorful-flowers-banner-animated-4k-blooming-flowers-background-frame-loop-video.jpg");
        background-repeat: repeat-y;
        background-position: top center;
        background-size: 100% auto;
    }
    
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    [data-testid="stApp"] {
        background: transparent;
    }
    .st-key-messagem p   {
        background-color: #eba0d1;
        padding: 10px;
        border-radius: 30px;
    }
    [data-baseweb="checkbox"] [data-testid="stWidgetLabel"] p {
        font-size: 1.3rem;
        width: 200px;
        margin-top: 0rem;
    }
    [data-baseweb="checkbox"] div {
        height: 2rem;
        width: 4rem;
    }
    [data-baseweb="checkbox"] div div {
        height: 2rem;
        width: 2.1rem;
    }
    [data-testid="stCheckbox"] label span {
        height: 2rem;
        width: 4rem;
    }
    </style>
""", unsafe_allow_html=True)


if aceitar:
    if input_name and input_lastname:
        novo_dados = pd.DataFrame([[input_name, input_lastname]],columns=["Nome", "Sobrenome"])
        if os.path.exists(names):
            df = pd.read_csv(names)
            df = pd.concat([df, novo_dados], ignore_index=True)
        else:
            df = novo_dados

        df.to_csv(names, index=False)
        st.success("Sua presença foi confirmada!")
        st.balloons()
    else:
        st.error("Preencha ambos os campos.")


st.subheader("Lista convidados")
on = st.toggle("Mostrar lista", key="toggle")

if on:
    if os.path.exists(names):
        df = pd.read_csv(names)
        st.dataframe(df)
    else:
        st.info("Nenhum dado cadastrado ainda.")
