#!/usr/bin/env python3

# dá para manipular o banco de dados por meio do vs code.
import sqlite3

con = sqlite3.connect("sql_example.db")
con.execute("PRAGMA foreign_keys = ON;")

#  é bom colocar as instruções em string multilinha
instructions = """\
INSERT INTO person (name, email, dept, role)
VALUES ('Bruno', 'bruno@rocha.com', 'Sales', 'Salesman');
---
INSERT INTO person (name, email, dept, role)
VALUES ('fulano', 'fulano@gomes.com', 'Sales', 'Manager');
"""

# adicionando informações ao banco de dados
for instruction in instructions.split("---"):
    # adicionando esse try except porque repetições de email não são aceitas, então se não puser isso, vai dar erro e o script não continua
    try:
        con.execute(instruction)
    except sqlite3.IntegrityError:
        continue

# para comandos do tipo DML (manipulation) é necessário dar commit
con.commit()

# para CONSULTAR as informacoes do banco de dados
# criando um cursor do banco de dados para comunicar com a tabela.
cur = con.cursor()

instruction = """\
SELECT id, name , email, dept, role
FROM person
WHERE dept = 'Sales';
"""

# retorna um objeto cursor, q é iterável.
# cada row é uma tupla
result = cur.execute(instruction)
print(result)
for row in result:
    print(row)  # tupla

print("*" * 50)
## "setando" o balance de uma pessoa ao adicionar no banco de dados (como no dundie)

instruction = """\
SELECT id, 500
FROM person
WHERE dept = 'Sales';
"""

# no sqlite, placeholder é a interrogação
# aqui, adicionando 500 para cada pessoa da tabela balance,
# como uma tupla contendo o id e o valor
result = cur.execute(instruction)
print(result)
for row in result:
    print(row)
    try:
        instruction = "INSERT INTO balance (person, value) VALUES (?, ?)"
        con.execute(instruction, row)
    except sqlite3.IntegrityError:
        continue

print("*" * 50)
con.commit()

#con = sqlite3.connect("sql_example.db")
#con.execute("PRAGMA foreign_keys = ON;")

# para usar a parte relacional do SQL são usados joins.
# nesse caso, primeiro pega as informações da banco de dados person
# e depois o do balance, pela coluna id na tabela person
# e coluna person na tabela balance (que são iguais)
instruction = """\
SELECT person.name, person.email, balance.value
FROM person
LEFT JOIN balance
WHERE person.id = balance.person
"""

result = cur.execute(instruction)

for row in result:
    print(row)
print("*" * 50)
