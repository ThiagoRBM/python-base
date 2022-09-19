#!/usr/bin/env python3

# pattern match estrutural

from turtle import Turtle  # biblioteca para aprendizado que vem com o python

print("""\
Jogo da tartaruga

comandos:
    move x y
    move steps
    turn angle (default 90)
    draw shape size (line | circle)
    write text
    stop | exit    
""")

turtle = Turtle()  # Turtle é uma classe
turtle.shape("turtle")
turtle.speed(3)
turtle.color("blue", "green")
turtle.shapesize(1.2, 1.2)
turtle.penup()

while True:
    # criar um loop que mantenha a tela aberta
    command: list[str] = input("🐢>    ").strip().split()
    # MANEIRA ANTIGA DE FAZER
    # if command[0] in ("exit", "stop", "q"):
    # break
    # if command[0] == "draw":
    # shape = command[1]
    # size = float(command[2])
    # turtle.pendown()  # se move desenhando, penup se move sem desenhar
    # if shape == "line":
    # turtle.forward(size)
    # elif shape == "circle":
    # turtle.circle(size)
    # MANEIRA USANDO PATTERN MATCH (comum em linguagens funcionais) PEP 636
    # switch case / Estrutural (no python se preocupa com estrutura de objeto e não com o valor)
    match command:  # ao invés de comparar com valor, insica qual a ESTRUTURA buscada. Pode usar classe, lista, etc.

        case ["move", *points]:
            #print(f"Movendo {points}")
            match points:  # verifica se foram passados 2 numeros
                case [x,y]:
                    turtle.goto(float(x), float(y))
                case [steps]:
                    turtle.forward(float(steps))
                case _:
                    print("Informar coordenadas ou passos")
            
        case ["turn", *options]:
                match options:
                    case [options]:
                        turtle.right(float(options))
                    case _:
                        turtle.right(90)
            #print(f"Rotacionando {options}")

        case ["draw", shape, size]:
            turtle.pendown()
            match shape:
                case "circle":  # aqui é equivalente ao if
                    turtle.circle(float(size))
                case "line":
                    turtle.forward(float(size))
            turtle.penup()
            #print(f"Desenhando {shape}, {size}")

        case ["write", *text]:
            turtle.write(" ".text, None, "center", 16, 20)
            #print(f"Escrevendo {text}")

        case ["exit" | "stop" | "q"]:
            break

        case _:  # opção final, caso nada dê match
            print("Comando inválido")
