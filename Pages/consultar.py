import streamlit as st; 
import Services.database as db


def consultar():
    st.title(":red[Consulta Cliente] ")
    colms = st.columns((1,2,2,5,4,3,3))
    campos = ['Nº','Nome','Idade','Email','Parcelas','Excluir','Alterar']
    for col, campo_nome in zip(colms,campos):
        col.write(campo_nome)

    for item in db.SelecionarTodos():
        col1, col2, col3, col4, col5, col6, col7 = st.columns((1,3,2,6,4,3,3))
        col1.write(item.id)
        col2.write(item.nome)
        col3.write(item.idade)
        col4.write(item.email)
        col5.write(item.parcelas)
        
        button_space_excluir = col6.empty()
        on_click_excluir = button_space_excluir.button('Excluir','btnExcluir' + str(item.id))
        button_space_alterar = col7.empty()
        on_click_alterar = button_space_alterar.button('Alterar','btnAlterar' + str(item.id))
        
        if on_click_excluir:
            db.Excluir(item.id)
            button_space_excluir.button('Excluido','btnExcluir' + str(item.id))
    
    
    with st.container():    
        st.write("Developer: [Instagram](https://www.instagram.com/israelsturaro/) || [GitHub](https://github.com/Israelsturaro)")   
