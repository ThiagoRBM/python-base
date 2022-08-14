#!/usr/bin/env python3

"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que frequentam cada uma das atividades
"""

__version__ = "0.1.0"
__author__ = "thiago"

sala1=["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2=["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles= ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica= ["Erik", "Carlos", "Maria"]
aula_danca= ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades=[("ingles",aula_ingles), 
            ("musica",aula_musica), 
            ("danca",aula_danca)]

for atividade in atividades:
    print()
    
    aula, alunos= atividade

    atvsala1= set(alunos) - set(sala2)
    atvsala2= set(alunos) - set(sala1)
    #atvsala1= set(sala1) & set(alunos) ## mesma coisa que acima, mas com interseção ao invés de diferença
    #atvsala2= set(sala2) & set(alunos) ## mesma coisa que acima, mas com interseção ao invés de diferença
    
    print(f"Alunos da sala 1 matriculados em {aula}: {atvsala1}")
    print(f"Alunos da sala 2 matriculados em {aula}: {atvsala2}")
    print("-" * 70)
    
