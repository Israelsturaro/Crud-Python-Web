import streamlit as str;
import models.Cliente as cliente
import Services.database as db
import pandas as pd
import Pages.Incluir as PagInclusão
import Pages.consultar as PagConsulta


#Maneira de Usar o Crud
#pip install streamlit
#Terminal--> streamlit run main.py


str.set_page_config(page_title="Crud_Web")
str.sidebar.title('Menu')


Page_Cliente = str.sidebar.selectbox('Cliente',['Incluir','Consultar'])
if Page_Cliente == 'Consultar':
    PagConsulta.consultar()
    
if Page_Cliente == 'Incluir':
    PagInclusão.incluir()




    
