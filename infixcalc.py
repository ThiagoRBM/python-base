#!/usr/bin/env python3

## minha linha de raciocínio acho que foi bem diferente da sua. Não mexi no código (tanto que tem lá o "len(sys.argv[1:]) == 0" para ficar parecida com a sua. Apesar de diferente ela funcionou direitinho, mas eu não tinha pensado em tratar todos os posíveis erros (porém, prometo que pausava e resolvia eles assim que você mencionava, antes de ver o resultado, e funcionou; apanhei só com o método "isdigit" porque não lembrava que era usado em str).
import os
import sys
from datetime import datetime

path = os.path.abspath(os.curdir)
# path= "/"
filepath = os.path.join(path, "calc_history.log")
timestamp = datetime.now().isoformat()
usr = os.getenv('USER', "annonymous")

operacao = None
n = [None, None]

operacoes = {
    "sum": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b
}

while True:

    if len(sys.argv[1:]) == 0:
        operacao = input("Digite uma operacao: ")
        if operacao not in operacoes.keys():
            print(f"Operacoes permitidas: {permitidas}")
            print(f"Operacao requisitada: `{operacao}`")
            sys.exit(1)
        n[0] = input("Digite um numero: ")
        n[1] = input("Digite outro numero: ")
    else:
        operacao = sys.argv[1]
        n = sys.argv[2:]

    numeros = []
    for num in n:
        if not num.replace(".", "").isdigit():
            print("Digitar apenas numeros para realizar a operação")
            print(f"Foi figitado: `{num}`")
            sys.exit(2)
        else:
            if "." in num:
                numeros.append(float(num))
            else:
                print("int")
                numeros.append(int(num))

    if len([operacao]) + len(numeros) != 3:
        print("Número de argumentos inválidos")
        print("ex: sum 5 5 ")
        sys.exit(3)

    resultado = operacoes[operacao](numeros[0], numeros[1])

    try:
        print(
            f"{timestamp} / {usr}: {operacao} of {numeros[0]} and {numeros[1]} equals {resultado}",
            file=open(filepath, "a"))
        print("Resultado armazenado em 'calc_history.log'.")
    except PermissionError as e:
        ## erro de permissão caso o arquivo esteja em pasta para a qual não temos permissão. Reprodução do erro na linha 47 ao invés da 48
        print(str(e))
        print("Resultado não armazenado.")
        sys.exit(4)

    print()
    print(resultado)
    print()

    cont = input(
        "Continuar a calcular? Enter para sim, qualquer outra tecla para não\n"
    ).strip().lower()

    if cont == "":
        sys.argv[1:] = []
        continue
    else:
        break
