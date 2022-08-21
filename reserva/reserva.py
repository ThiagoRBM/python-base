#!/usr/bin/env python3

""" Faça um programa de terminal que exibe ao usuário uma lista dos quartos
disponíveis para alugar e o preço de cada quarto. Esta informação está 
disponível em um arquivo de texto separado por vírgulas.

'quartos.txt'
#codigo,nome,preço
1,Suite Master,500
2,Quarto Familia,200
3,Quarto Single,100
4,Quarto Simples,50

O programa pergunta ao usuario o nome, qual o número do quarto a ser 
reservado e a quantidade de dias. No final exibe o valor estimado a ser
pago.

O programa deve salvar esta escolha em outro arquivo contendo as 
reservas.

'reservas.txt'
#cliente,quarto,dias
thiago,3,12

Se outro usuario tentar reservar o mesmo quarto o programa deve exibir
uma mensagem informando que ja esta reservado.
"""

from datetime import datetime
import os
import sys

path= os.path.abspath(os.curdir)
lista_quartos= os.path.join(path,"quartos.txt")

if os.path.exists(os.path.join(path,"reservas.txt")):
    lista_reservas= os.path.join(path,"reservas.txt")
### verificando se exite um arquivo com reservas (se sim, verificando
### os codigos das reservas feitas)
    reservas_feitas=[]
    for l in open(lista_reservas):
        reservas_feitas.append(l.split(","))

    codigos_reservas=[]
    for i in reservas_feitas:
        nome,codigo= i[3].split(":")
        codigos_reservas.append(codigo.strip())
else:
    codigos_reservas=[]

quartos=[]
try:
    with open(lista_quartos) as quarto_lista:
        next(quarto_lista)
        for l in quarto_lista:
        ## armazenando o arquivo com as opções e informações de quartos
        ## em uma lista e mostrando no console
            codigo,nome,preco= l.strip().split(",")
            dic={"codigo": codigo,
                "nome": nome,
                "preco": preco,
                "disponibilidade": ("\U00002705" if codigo not in codigos_reservas
                                    else "\U0001F6AB")}
            quartos.append(dic)
except FileNotFoundError:
    print("Informações sobre quartos indisponíveis.")
    sys.exit(2)

codigos_disponiveis= ([quarto["codigo"] for quarto in quartos[1:] 
                        if quarto["codigo"] not in codigos_reservas])

if len(quartos) == len(codigos_reservas):
    print("Hotel lotado.")
    sys.exit(1)

print(" " + "-"*49 + " ")
print(f"| {' '*4} | {'Codigo':^7} | {'Quarto':^20} | {'Preco':^7} |")
print(" " + "-"*49 + " ")
for i in quartos:
    print(f"| {i['disponibilidade']:^3} | {i['codigo'].title():^7} | " 
            f"{i['nome'].title():^20} | {i['preco'].title():^7} |")
    print(" " + "-"*49 + " ")

nome_cliente= input("Digite o nome usado para fazer a reserva ou <enter>"
                " para cancelar:\n").title().strip()
print()
if nome_cliente == 0 or nome_cliente.replace(".","").isdigit():
    print("Digitar um nome válido.")
    sys.exit(1)

codigo_cliente= input("Digite o codigo do quarto:\n").strip()
if codigo_cliente not in [quarto["codigo"] for quarto in quartos[1:]]:
    print(f"Quarto de código `{codigo_cliente}` inexistente.")
    sys.exit(3)
elif not codigo_cliente in codigos_disponiveis:
    print(f"Quarto {codigo_cliente} reservado.\n"
            f"Reserva não realizada.")
    sys.exit(4)
   
dias= input("Digite quantos dias de reserva:\n").strip()
if not dias.replace(".","").isdigit() or float(dias) <= 0:
    print(f"Favor usar apenas números maiores que 0 no campo. "
            f"Número utilizado: {dias}")
    sys.exit(5)

reserva= {"nome_cliente": nome_cliente,
            "dias": dias,
            "quarto": codigo_cliente}
for i in range(1,len(quartos)):
    if codigo_cliente in quartos[i].get("codigo"):
        reserva["total"]= float(quartos[i].get("preco")) * float(dias)

print(f"Confirmar reserva do quarto {reserva['nome_cliente']}, "
        f"de código {reserva['quarto']}, " 
        f"por {dias} dias. "
        f"Valor total: {reserva['total']}")
    
if input("Pressione <enter> para continuar ou qualquer outra tecla"
        "para cancelar a compra:\n") != "":
        sys.exit(6)

with open(os.path.join(path,"reservas.txt"), "a") as file_:
    file_.write(f"DATA:{datetime.now().isoformat()},")
    for info in reserva.keys():
        file_.write(f"{info}:{reserva[info]},")
    file_.write("\n")

print("Reserva realizada com sucesso.")

