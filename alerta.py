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

while True:

    try:
        temp= float(input("Digite a temperatura (°C): ").strip())
        umid= float(input("Digite a umidade: ").strip())
    except ValueError as e:
        print(str(e)) ## dá para fazer isso com logging
        sys.exit(1)

    if temp >= 45:
        print("ALERTA!!! Perigo calor extremo")
    elif temp > 30 and temp * 3 >= umid:
        print("ALERTA!!! Perigo calor úmido")
    elif temp >= 10 and temp <= 30:
        print("Condições normais")
    elif temp >=0 and temp <10:
        print("Frio")
    elif temp < 0:
        print("ALERTA!!! Frio extremo")

    if input("Deseja continuar?" 
    "[Sim= enter, não= Qualquer outra tecla]\n") != "":
        break
     
