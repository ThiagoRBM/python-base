#!/usr/bin/env python3

""" Alarme de temperatura

Script que pergunta ao usuário a temperatura atual e o índice de umidade do ar. Mensagens de alerta serão exibidas nas seguintes condições:
    temp maior que 45: ALERTA!!! Perigo calor extremo
    temp vezes 3 maior maior ou igual a umidade: ALERTA!!! Perigo calor úmido
    temp entre 10 e 30: Normal
    temp entre 0 e 10: Frio
    temp < 0: ALERTA!!! Frio extremo
"""

import sys


def reads_input():

    """Recebe informações do usuário e retorna um dicionário com 2 keys."""
    climate_dict= {}
    climate=["temp", "umid"]
    message=["Digite a temperatura (°C): ",
                "Digite a umidade: "]
    try:
        for i , data in enumerate(climate):
            climate_dict[climate[i]]= float(input(message[i]).strip())
    except ValueError as e:
        print(str(e)) ## dá para fazer isso com logging
        sys.exit(1)
    return climate_dict


while True:
    info= reads_input()

    if info["temp"] >= 45:
        print("ALERTA!!! Perigo calor extremo")
    elif info["temp"] > 30 and info["temp"] * 3 >= info["umid"]:
        print("ALERTA!!! Perigo calor úmido")
    elif info["temp"] >= 10 and info["temp"] <= 30:
        print("Condições normais")
    elif info["temp"] >=0 and info["temp"] <10:
        print("Frio")
    elif info["temp"] < 0:
        print("ALERTA!!! Frio extremo")

    if input("Deseja continuar?" 
    "[Sim= enter, não= Qualquer outra tecla]\n") != "":
        break
     
