#!/usr/bin/env python3

import os
import sys

import logging

#print(f"{sys.argv=}")
#print(f"{sys.argv[1]=}")

## BOILERPLATE (aula de logs)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("thiago", log_level)
ch = logging.StreamHandler()  # Console/terminal/stderr. Pode ser formatado
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

args= {"lang" : None,
        "count" : None}

for arg in sys.argv[1:]:
    #print(arg)

    # EAFP
    try:
        key, value= str(arg).split(sep="=")
    except ValueError as e:
        log.error(
            "Você usou %s, tente usar --key=value. Erro: %s",
            arg,
            str(e)
        )
        sys.exit(1)

    key= key.lstrip("-").strip()
    value= value.strip()
    if key not in args.keys():
            print(f"Argumento: `{key.lstrip('-')}` não reconhecido")
            sys.exit(2)
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

if args["count"] is None:
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

# EAFP
try:
    mensagem= f"{msg[current_language]}\n"
except:
    print(f"Língua escolhida: {args['lang']}")
    print(f"Línguas disponíveis: {list(msg.keys())}")
    sys.exit(3)

print(f"{mensagem * count}")
