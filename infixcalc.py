#!/usr/bin/env python3

## minha linha de raciocínio acho que foi bem diferente da sua. Não mexi no código (tanto que tem lá o "len(sys.argv[1:]) == 0" para ficar parecida com a sua. Apesar de diferente ela funcionou direitinho, mas eu não tinha pensado em tratar todos os posíveis erros (porém, prometo que pausava e resolvia eles assim que você mencionava, antes de ver o resultado, e funcionou; apanhei só com o método "isdigit" porque não lembrava que era usado em str).
import sys

operacao= None
n= [None, None]

if len(sys.argv[1:]) == 0:
    operacao= input("Digite uma operacao: ")
    n[0]= input("Digite um numero: ")
    n[1]= input("Digite outro numero: ")
else:
    operacao= sys.argv[1]
    n= sys.argv[2:]
    
numeros= []
for num in n:
    if num.replace(".","").isdigit():
        if "." in num:
            numeros.append(float(num))
        else:
            numeros.append(int(num))
    else:
        print("Digitar apenas numeros para realizar a operação")
        print(f"Foi figitado: `{num}`")
        sys.exit(1)
        
if len([operacao]) + len(numeros) != 3:
    print("Número de argumentos inválidos")
    print("ex: sum 5 5 ")
    sys.exit(2)

permitidas= ["sum","difference","product","quotient"]
if operacao not in permitidas:
    print(f"Operacoes permitidas: {permitidas}")
    print(f"Operacao requisitada: `{operacao}`")
    sys.exit(3)
    
operacoes= {"sum": numeros[0] + numeros[1],
            "difference": numeros[0] - numeros[1],
            "product": numeros[0] * numeros[1],
            "quotient": numeros[0] / numeros[1]}

print(operacoes[operacao])
