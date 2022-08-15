#!/usr/bin/env python3

import os
import sys

#print(f"{sys.argv=}")
#print(f"{sys.argv[1]=}")

args= {"lang" : None,
        "count" : None}

for arg in sys.argv[1:]:
    key, value= str(arg).split(sep="=")
    key= key.lstrip("-").strip()
    value= value.strip()
    if key not in args.keys():
            print(f"Argumento: `{key.lstrip('-')}` não reconhecido")
            sys.exit()
    args[key]= value
    #print(arg)
#print(args)
    
if args["lang"] is None:
    current_language = os.getenv("LANG")
    if current_language is None:
        current_language= input("Choose your language: ")
else:
    current_language= args["lang"]

#print(current_language)
#print(args["count"])

if args["count"] == None:
    #print("aqui")
    count = 1
else:
    count= int(args["count"])
#print(count)

###################################################
# ALTERE daqui usando dicionários
###################################################

msg= {"en_US" : "Hello, World!",
        "pt_BR" : "Olá, Mundo!",
        "it_IT" : "Ciao, Mondo!",
        "es_SP" : "Hola, Mundo!",
        "fr_FR" : "Bonjour, Monde!"}

mensagem= f"{msg[current_language]}\n"

print(f"{mensagem * count}")
