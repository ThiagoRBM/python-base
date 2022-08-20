#!/usr/bin/env python3

vogais= ["a","e","i","o","u"]
texto= []

while True:
    palavra= input("Digite uma palavra ou <enter> para sair: ")
    if palavra == "":
        break

    duplicada=""
    for letra in palavra:
        if letra in vogais or letra in [l.upper() for l in vogais]:
            duplicada= duplicada + letra*2
        else:
            duplicada= duplicada + letra
        
    texto.append(duplicada)
    

#for palavra in texto:
#    print(palavra)
# o loop acima pode ser substituido por (o * significando novamente desempacotamento):
print(*texto, sep="\n")
