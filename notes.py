#!/usr/bin/env python3
"""Bloco de notas

$ notes.py new "Minha nota"
tag: tech
text:
Anotacao geral sobre carreira de tecnologia.

$ notes.py read --tag=tech
...
...
"""
__version__ = "0.0.1"
__version__ = "thiago"

import os
import sys

path= os.path.abspath(os.curdir)
filepath= os.path.join(path, "notepad.txt")

arguments= sys.argv[1:]

permitidas= ["new", "read"]
func= arguments[0]

if func not in permitidas:
    print(f"Funcoes permitidas: {permitidas}")
    print(f"Funcao solicitada: '{func}'")
    sys.exit(1)

if func == "new":
    while True:
        arg_dict= {}
        
        if not arguments[1:]:
            print("Fornecer uma tag para a entrada.")
            arg_dict["tag"]= input("Digite a tag: ").strip()
            print("Fornecer um texto para a entrada.")
            arg_dict["text"]= input("Digite o texto: ").strip()

        else:
            for i in arguments[1:]:
                key,value= i.split("=")
                arg_dict[key]=value
        
        if "tag" not in list(arg_dict.keys()) or "text" not in list(arg_dict.keys()):
            print(f"Usar argumentos 'tag' e 'text'.")
            print(f"Argumentos usados: {arg_dict.keys()}")
            sys.exit(2)
            
        with open(filepath, "a") as file_:
            for i in arg_dict:
                file_.writelines(f"{i}: {arg_dict[i]}\n")
            file_.write("." * 78 + "\n")
            file_.write("\n")
            print(f"informações salvas em {filepath}")

        novo_post= input("Deseja adicionar mais uma entrada? [sim/nao]\n")
        if novo_post.strip().lower() == "sim":
            continue 
        elif novo_post.strip().lower() == "nao":
            break

if func == "read":
    arg_dict= {}

    if not arguments[1:]:
        print("É necessário informar um caminho para o arquivo a ser lido.")
        arg_dict["filepath"]= input("Caminho: ")
        arg_dict["tag"]= input("Fornecer a tag procurada: ").strip()
    
    else:
        for i in arguments[1:]:
            key,value= i.split("=")
            arg_dict[key]=value

    if "filepath" not in list(arg_dict.keys()) or "tag" not in list(arg_dict.keys()):
        print(f"Usar argumentos 'filepath' e 'tag'.")
        print(f"Argumentos usados: {arg_dict.keys()}")
        sys.exit(3)
    
    file_= open(arg_dict["filepath"]) # notepad.txt
    content= file_.read().split("\n\n")

    if arg_dict["tag"] not in content:
        print("Sem entradas da tag procurada.")

    for l in content:
        if arg_dict["tag"] in l:
            print(l)
 
