import mysql.connector as mysql
from database.conexao import conectar

class Animal():
    # Constructor da classe Animal com todos os atributos da tabela animal
    def __init__(self, animal_id, apelido, especie, nome_cientifico, peso, data_nascimento, data_chegada, dieta, rotina_limpeza, recinto, ativo):
        self.animal_id = animal_id
        self.apelido = apelido
        self.especie = especie
        self.nome_cientifico = nome_cientifico
        self.peso = peso
        self.data_nascimento = data_nascimento
        self.data_chegada = data_chegada
        self.dieta = dieta
        self.rotina_limpeza = rotina_limpeza
        self.recinto = recinto

        self.ativo = ativo

    @staticmethod
    def listar_animais():
        conn = conectar()
        if conn is None:
            return []
        cursor = conn.cursor()

        listar = "select * from animal where ativo = %s"
        valores = (True,)
        cursor.execute(listar, valores)

        resultados = cursor.fetchall()
        animais = []

        for r in resultados: # Para cada registro retornado do banco de dados, cria um objeto Animal
            animal = Animal(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10])
            animais.append(animal)

        cursor.close()
        conn.close()

        return animais

    @staticmethod
    def filtrar_animais(especie, recinto):
        conn = conectar()
        if conn is None:
            return []
        cursor = conn.cursor()

        filtrar = "select * from animal where ativo = %s"
        valores = [True]

        if especie:
            filtrar += " and especie = %s"
            valores.append(especie)
        
        if recinto:
            filtrar += " and recinto = %s"
            valores.append(recinto)

        cursor.execute(filtrar, tuple(valores)) # Converte a lista de valores em tupla

        resultados = cursor.fetchall()
        animais = []

        for r in resultados:
            animal = Animal(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10])
            animais.append(animal)

        cursor.close()
        conn.close()

        return animais
    
    @staticmethod
    def salvar_animal(apelido, especie, nome_cientifico, peso, data_nascimento, data_chegada, dieta, rotina_limpeza, recinto):
        conn = conectar()
        if conn is None:
            return False
        cursor = conn.cursor()

        inserir = "insert into animal (apelido, especie, nome_cientifico, peso, data_nascimento, data_chegada, dieta, rotina_limpeza, recinto, ativo) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (apelido, especie, nome_cientifico, peso, data_nascimento, data_chegada, dieta, rotina_limpeza, recinto, True)

        try:
            cursor.execute(inserir, valores)

            conn.commit()
            cursor.close()
            conn.close()

            return True
        except:
            print(f"Erro ao salvar animal: {e}")
            cursor.close()
            conn.close()
            return False


    def remover_animal(self,):
        conn = conectar()
        if conn is None:
            return False
        cursor = conn.cursor()

        remover = "update animal set ativo = %s where animal_id = %s"
        valores = (False, self.animal_id)
        cursor.execute(remover, valores)

        conn.commit() # Confirma a transação no banco de dados
        cursor.close()
        conn.close()
        return True
    
    def abrir(usuario):
        print(usuario.nome)
        print(usuario.admin)