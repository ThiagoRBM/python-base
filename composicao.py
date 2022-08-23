#!/usr/bin/env python3

names= ["thiago",
        "joao",
        "rafael",
        "Rafaela",
        "ronaldo",
        "joana"]

## estilo funcional
print(*list(filter(lambda nome: nome[0].lower() == "r", names)),sep="\n")
print()

## estilo imperativo
def comeca_b(texto):
    return texto[0].lower() == "r"

filtro= filter(comeca_b,names)
filtro= list(filtro)
for i in filtro:
    print(i)

