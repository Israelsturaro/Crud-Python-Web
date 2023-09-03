import mysql.connector
import models.Cliente as cliente


conx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="crud_python"
)
mycursor = conx.cursor()

def connect(cliente):
    sql = "INSERT INTO cliente (nome, idade, email, parcelas) VALUES (%s,%s,%s,%s)"
    val = (cliente.nome, cliente.idade, cliente.email, cliente.parcelas)
    mycursor.execute(sql,val)
    conx.commit()
    
def Excluir(cliente):
    sql = "DELETE FROM cliente WHERE id = %s"
    val = (cliente.id)
    mycursor.execute(sql,val)
    conx.commit()
    

def SelecionarTodos():
    mycursor.execute("SELECT * FROM cliente")
    costumerlist = []
    
    for row in mycursor.fetchall():
        costumerlist.append(cliente.Cliente(row[0],row[1],row[2],row[3],row[4]))

    return costumerlist