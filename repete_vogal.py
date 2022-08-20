#!/usr/bin/env python3

"""Peça ao usuário que digite uma ou mais palavras e imprima cada uma com as vogais duplicadas

e.g.: Python -> Pythoon
"""

vogais= ["a", "e", "i", "o", "u"]

while True:
    texto= input("Digite uma ou mais palavras ou <enter> para sair: ")

    ls=[]
    for letra in texto:
        if letra in vogais or letra in [v.upper() for v in vogais]:
            letra= letra*2
            ls.append(letra)
        else:
            ls.append(letra)

    print("".join(ls))

    if texto == "":
        break
