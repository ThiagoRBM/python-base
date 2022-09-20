#!/usr/bin/env python3
#  usar extensão SQLite
#  ferramenta que ajuda a modelar banco de dados app.dbdesigner.net, roda no
#  navegador
import sqlite3  # vem com o python, nao precisa instalar

con = sqlite3.connect(
    "sql_example.db"
)  # se conecta a um arquivo ou cria um banco de dados efêmero com :memory:
con.execute("PRAGMA foreign_keys = ON ; ")  # habilita a parte relacional
#  do SQL. Outros como MySQL e POSTGRESQL já são assim por padrão

# instrucao para criar a tabela,
# sera chamada person
# banco de dados baseado em schema
# precisa especificar os tipos e etc
# UNIQUE NOT NULL sao constraints
instruction = """\
CREATE TABLE if not exists person (
    id integer PRIMARY KEY AUTOINCREMENT,
    name varchar NOT NULL,
    email varchar UNIQUE NOT NULL,
    dept varchar NOT NULL,
    role varchar NOT NULL
);
"""

#  cria a outra tabela
#  na ultima instrucao, uma tabela balance, e o campo
#  person dela é uma chave de outra tabela (id da tabela pessoa, acima)
# instruction = """\
# CREATE TABLE if not exists balance (
#     id integer PRIMARY KEY AUTOINCREMENT,
#     person integer UNIQUE NOT NULL,
#     value integer NOT NULL,
#     FOREIGN KEY(person) REFERENCES person(id)
# );
# """

instructions = """\
CREATE TABLE if not exists person (
id integer PRIMARY KEY AUTOINCREMENT,
name varchar NOT NULL,
email varchar UNIQUE NOT NULL,
dept varchar NOT NULL,
role varchar NOT NULL
);
---
CREATE TABLE if not exists balance (
id integer PRIMARY KEY AUTOINCREMENT,
person integer UNIQUE NOT NULL,
value integer NOT NULL,
FOREIGN KEY(person) REFERENCES person(id)
);
---
CREATE TABLE if not exists movement (
id integer PRIMARY KEY AUTOINCREMENT,
person integer NOT NULL,
value integer NOT NULL,
date datetime NOT NULL,
actor varchar NOT NULL,
FOREIGN KEY(person) REFERENCES person(id)
);
---
CREATE TABLE if not exists user (
id integer PRIMARY KEY AUTOINCREMENT,
person integer UNIQUE NOT NULL,
password varchar NOT NULL,
FOREIGN KEY(person) REFERENCES person(id)
);
"""

for instruction in instructions.split("---"):
    #  criando multiplas tabelas de uma vez
    con.execute(instruction)

#  con.commit()  # importante depois dos comandos serem dados, ser feito o
# commit quando usado o DML

con.close(
)  # fechar a conexao. Assim como com o open(arquivo), seria possível fazer
#  dentro de um gerenciador de contexto
