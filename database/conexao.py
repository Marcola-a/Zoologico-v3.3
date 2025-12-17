import os
import mysql.connector as mysql
from mysql.connector import Error # Importa o tipo de erro do MySQL

def conectar():
    host = os.environ.get("DB_HOST", "localhost")
    user = os.environ.get("DB_USER", "root")
    password = os.environ.get("DB_PASSWORD", "mysql")
    database = os.environ.get("DB_NAME", "zoologico")
    conexao = None
    try:
        conexao = mysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if conexao.is_connected():
            return conexao
    except Error as e:
        # Em aplicações reais, logar o erro seria preferível a print
        print("Erro ao conectar ao MySQL:", e)
        return None


"""
cursor = conexao.cursor() # Cria um objeto cursor para executar comandos SQL
cursor.execute("select * from animal;")


for r in cursor:
    print(r)   
"""