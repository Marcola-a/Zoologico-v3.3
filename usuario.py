import mysql.connector as mysql
from database.conexao import conectar

class Usuario():
    def __init__(self, id_usuario, nome, senha, email, admin):
        self.usuario_id = id_usuario
        self.nome = nome
        self.senha = senha
        self.email = email
        self.admin = bool(admin)

    @staticmethod
    def autenticar(nome, senha):
        conn = conectar()
        if conn is None:
            return False
        cursor = conn.cursor()

        verificar = "select * from usuario where nome = %s AND senha = %s"
        valores = (nome, senha)
        cursor.execute(verificar, valores)

        resultado = cursor.fetchone()
        
        cursor.close()
        conn.close()

        if resultado:
            return Usuario(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4])
        else:
            return None
    
    @staticmethod
    def novo_usuario(nome, senha, email):
        conn = conectar()
        if conn is None:
            return None
        cursor = conn.cursor()

        inserir = "insert into usuario (nome, senha, email, admin) values (%s, %s, %s, %s)"
        valores = (nome, senha, email, False)
        cursor.execute(inserir, valores)

        conn.commit() # Confirma a transação no banco de dados
        inserted_id = cursor.lastrowid # Pega o ID do usuário inserido
        cursor.close()
        conn.close()
        return inserted_id