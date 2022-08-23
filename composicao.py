#!/usr/bin/env python3

names= ["thiago",
        "joao",
        "rafael",
        "Rafaela",
        "ronaldo",
        "joana"]

print(*list(filter(lambda nome: nome[0].lower() == "r", names)),sep="\n")
