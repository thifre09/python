from typing import Any
from enum import Enum
import pandas as pd

class Database():
    def __init__(self, nome: str = "thifreBD"):
        self.nome: str = nome
        self.tabelas: dict[str, Tabela] = {}

class Tabela():
    def __init__(self, nome: str):
        self.nome: str = nome
        self.colunas: dict[str, Coluna] = {}

class Coluna():
    def __init__(self, nome: str, tipo: Any):
        self.nome: str = nome
        self.tipo: Any = tipo

class Registro():
    pass

class AutoIncremento():
    def __init__(self, valor_inicial: int = 1):
        self.valor_atual: int = valor_inicial

    def proximo_valor(self) -> int:
        self.valor_atual += 1
        return self.valor_atual
    
def create():
    global wordIndex, context, words, databases
    wordIndex += 1
    if (words[wordIndex] == "database"):
        if (len(words) <= wordIndex + 1):
            d = Database()
            databases[d.nome] = d
            context = d.nome
        else:
            d = Database(words[wordIndex + 1])
            databases[d.nome] = d
            context = d.nome
            wordIndex += 1
    elif (words[wordIndex] == "table"):
        if (context == ""):
            print("Nenhum banco de dados selecionado. Use CREATE DATABASE primeiro.")
            return
        if (wordIndex + 1 >= len(words)):
            print("Comando CREATE TABLE inválido.")
            return
        else:
            wordIndex += 1
            t = Tabela(words[wordIndex])
            databases[context].tabelas[t.nome] = t
    else:
        print("Comando CREATE inválido.")

def alter():
    # alter
    global wordIndex, context, words, databases
    wordIndex += 1
    if (words[wordIndex] == "database"):
        # alter database
        wordIndex += 1
        if (len(words) < wordIndex + 4):
            print("Comando ALTER DATABASE inválido.")
            return
        else:
            if (words[wordIndex + 1] == "rename" and words[wordIndex + 2] == "to"):
                old_name = words[wordIndex]
                new_name = words[wordIndex + 3]
                databases[new_name] = databases.pop(old_name)
                databases[new_name].nome = new_name
                context = new_name
                wordIndex += 3
            else:
                print("Comando ALTER DATABASE inválido.")
                return

    elif (words[wordIndex] == "table"):
        # alter table
        wordIndex += 1
        if (len(words) <= wordIndex + 3 and words[wordIndex + 1] == "rename" and words[wordIndex + 2] == "to"):
            old_name = words[wordIndex]
            new_name = words[wordIndex + 3]

            t = databases[context].tabelas[old_name]
            t.nome = new_name
            del databases[context].tabelas[old_name]

            databases[context].tabelas[new_name] = t
            wordIndex += 3
        elif (len(words) <= wordIndex + 4 and words[wordIndex + 1] == "add" and words[wordIndex + 2] == "column"):
            # alter table [nome]
            t = databases[context].tabelas[words[wordIndex]]
            column_name = words[wordIndex + 3]
            type_name = words[wordIndex + 4]
            match type_name:
                case "int":
                    t.colunas[column_name] = Coluna(column_name, int)
                case "str":
                    t.colunas[column_name] = Coluna(column_name, str)
                case "float":
                    t.colunas[column_name] = Coluna(column_name, float)
                case "enum":
                    if (len(words) <= wordIndex + 5):
                        print("Comando ALTER TABLE ADD COLUMN inválido para tipo ENUM.")
                        print("Especifique os valores do ENUM entre parênteses.")
                        print("Exemplo: ALTER TABLE tabela1 ADD COLUMN status enum (ativo, inativo, pendente)")
                        return
                    enum_values = words[wordIndex + 5].strip("()").split(",")
                    enum_type = Enum(words[wordIndex] + column_name + "Enum", {val: val for val in enum_values})
                    t.colunas[column_name] = Coluna(column_name, Enum)
                    t.colunas[column_name].enum_type = enum_type
                case "bool":
                    t.colunas[column_name] = Coluna(column_name, bool)

        else:
            print("Comando ALTER TABLE inválido.")
            return
            
    elif (words[wordIndex] == "context"):
        wordIndex += 1
        if (len(words) < wordIndex + 4):
            print("Comando ALTER CONTEXT inválido.")
            return
        else:
            if (words[wordIndex] == "to" and words[wordIndex + 1] == "database"):
                new_db = words[wordIndex + 2]
                if new_db in databases:
                    context = new_db
                    wordIndex += 2
                else:
                    print(f"Banco de dados '{new_db}' não existe.")
                    return
    else:
        print("Comando ALTER inválido.")

def drop():
    global wordIndex, context, words, databases
    wordIndex += 1
    if (words[wordIndex] == "database"):
        wordIndex += 1
        db_name = words[wordIndex]
        if db_name in databases:
            del databases[db_name]
            if context == db_name:
                context = ""
        else:
            print(f"Banco de dados '{db_name}' não existe.")
    elif (words[wordIndex] == "table"):
        wordIndex += 1
        table_name = words[wordIndex]
        if context == "":
            print("Nenhum banco de dados selecionado. Use CREATE DATABASE primeiro.")
            return
        if table_name in databases[context].tabelas:
            del databases[context].tabelas[table_name]
        else:
            print(f"Tabela '{table_name}' não existe no banco de dados '{context}'.")
    else:
        print("Comando DROP inválido.")

def insert():
    pass

def select():
    pass

def help():
    print("""
Comandos disponíveis: CREATE, ALTER, DROP, INSERT, SELECT, HELP
Outras palavras-chave: DATABASE, TABLE, CONTEXT, RENAME, TO, ADD, COLUMN

create database [nome] - Cria um banco de dados com o nome especificado. Se nenhum nome for fornecido, o nome padrão 'thifreBD' será usado.
create table [nome] - Cria uma tabela no banco de dados atual com o nome especificado.
          
alter database [nome] rename to [novo_nome] - Renomeia o banco de dados atual para o novo nome especificado.
alter table [nome] rename to [novo_nome] - Renomeia a tabela especificada para o novo nome.
alter context to database [nome] - Muda o contexto atual para o banco de dados especificado.
          
alter table [nome] add column [coluna] [tipo] - Adiciona uma nova coluna à tabela especificada com o tipo de dado fornecido (int, str, float, enum, bool).
alter table [nome] add column [coluna] enum ([valores]) - Adiciona uma nova coluna do tipo ENUM à tabela especificada com os valores fornecidos.
*alter table [nome] alter column [coluna] set type [tipo] - Altera o tipo de dado da coluna especificada na tabela.
*alter table [nome] alter column [coluna] set enum ([valores]) - Altera os valores do tipo ENUM da coluna especificada na tabela.
*alter table [nome] alter column [coluna] rename to [novo_nome] - Renomeia a coluna especificada na tabela.
*alter table [nome] drop column [coluna] - Remove a coluna especificada da tabela.
          
drop database [nome] - Remove o banco de dados especificado. 
drop table [nome] - Remove a tabela especificada do banco de dados atual.
          
*insert on [tabela] ([colunas]) values ([valores]) - Insere um novo registro na tabela especificada com os valores fornecidos para as colunas listadas.

*select [colunas] from [tabela] where [condição] - Seleciona e exibe os registros da tabela especificada que atendem à condição fornecida.
        
help - Exibe esta mensagem de ajuda.      
""")

def main():
    global wordIndex, context, words
    while True:
        input_string = input("thifreBD> ")
        input_string = input_string.lower()
        words = input_string.split(" ")
        wordIndex = 0
        if (words[0] not in keywords.keys()):
            print("Comando inválido.")
            continue
        while (wordIndex < len(words)):
            try:
                keywords[words[wordIndex]]()
                wordIndex += 1
            except:
                wordIndex += 1
                continue

context: str = ""
words: list[str] = []
wordIndex: int = 0
keywords: dict[str, object] = {
    "create": create,
    "alter": alter,
    "help": help
}

databases: dict[str, Database] = {}

if __name__ == "__main__":
    main()

