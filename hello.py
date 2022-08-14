#!/usr/bin/env python3

import os

current_language = os.getenv("LANG", "en_US")[:5]

###################################################
# ALTERE daqui usando dicionários
###################################################

msg= {"en_US" : "Hello, World!",
        "pt_BR" : "Olá, Mundo!",
        "it_IT" : "Ciao, Mondo!",
        "es_SP" : "Hola, Mundo!",
        "fr_FR" : "Bonjour, Monde!"}

print(msg[current_language])
