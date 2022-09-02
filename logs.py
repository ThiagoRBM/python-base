#!/usr/bin/env python3

import os
import logging
from logging import handlers

# BOILERPLATE (código que precisa ser repetida muitas vezes)
# mas ele pode ser substituido por uma funcao que faz tudo isso, sem repeticao ou mesmo uma lib especifica para isso
## configuração de logs para o programa
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("bruno", log_level)

#ch = logging.StreamHandler()  # Console/terminal/stderr. Pode ser formatado
#ch.setLevel(log_level)

fh = handlers.RotatingFileHandler( ## formata a mensagem de log e exporta para um arquivo
   "meulog.log", 
   maxBytes=300, # 10**6
   backupCount=10, ## numero de arquivos de log a serem mantidos (se 1, aquando o tamanho máximo for atingido, o informações anteriores serão sobrescritas)
)
fh.setLevel(log_level)
fmt = logging.Formatter( ## as variáveis a serem usadas na substituicao estão são documentadas no site da lib
    '%(asctime)s  %(name)s  %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
# ch.setFormatter(fmt)
fh.setFormatter(fmt)
#log.addHandler(ch)
log.addHandler(fh) ## o handler "decide" o que fazer com o log


"""
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuarios")
log.warning("Aviso que nao causa erro")
log.error("Erro que afeta uma unica execucao")
log.critical("Erro geral ex: banco de dados sumiu")
"""

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))
