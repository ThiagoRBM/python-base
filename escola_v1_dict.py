#!/usr/bin/env python3

"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que frequentam cada uma das atividades
"""

__version__ = "0.1.0"
__author__ = "thiago"

salas= {"sala1" : {"Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"},       "sala2" : {"Joao", "Antonio", "Carlos", "Maria", "Isolda"}}

aulas= {"ingles" : {"Erik", "Maia", "Joana", "Carlos", "Antonio"},
        "musica" : {"Erik", "Carlos", "Maria"},
        "danca"  : {"Gustavo", "Sofia", "Joana", "Antonio"}}

for alunos in aulas.items():
    aula= alunos[0]
    matriculados= alunos[1]

    atvsala1= salas["sala1"] & matriculados
    atvsala2= salas["sala2"] & matriculados

    print(f"Alunos da sala 1 matriculados em {aula}: {atvsala1}")
    print(f"Alunos da sala 2 matriculados em {aula}: {atvsala2}")
    print("-" * 70)

