import streamlit as str;
import models.Cliente as cliente
import Services.database as db
import pandas as pd

def incluir():
    str.title(":blue[Cadastro Clientes] ")
    with str.form(key="Create_Clientes"):
        input_name = str.text_input(label="Nome: ",placeholder="Digite seu nome Completo",autocomplete="off")
        input_idade = str.number_input(label="idade: ",format="%d",step=1,)
        input_email = str.text_input(label="Email: ",placeholder="Digite Aqui!",autocomplete="off")
        input_Parcelas = str.selectbox("Selecione Quantidade de Parcelas",["1x","2x","3x","4x","5x","6x","7x","8x","9x","10x","11x","12x"])
        input_button_submit = str.form_submit_button("Enviar") 
    with str.container():    
        str.write("Developer: [Instagram](https://www.instagram.com/israelsturaro/) || [GitHub](https://github.com/Israelsturaro)")   

    if  input_button_submit:
        cl = cliente.Cliente(0,input_name, input_idade,input_email,input_Parcelas)
        db.connect(cl)
        str.success("Cliente Cadastrado Com sucesso")
