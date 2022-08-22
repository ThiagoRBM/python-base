#!/usr/bin/env python3
"""Exemplos de envio de e-mail"""
import smtplib

SERVER = "localhost"
PORT = 8025 ## por padrão a porta para servidor de email é a 25, mas a porta 8025 é um servidor do python de teste

FROM = "bruno@rocha.com"
TO = ["destino1@server.com", "destino2@server.com"]
SUBJECT = "Meu e-mail via Python"
TEXT = """\
Este é o meu e-mail enviado pelo Python
<b>Olá mundo</b>
"""

# SMTP
message = f"""\
From: {FROM}
To: {", ".join(TO)}
Subject: {SUBJECT}
{TEXT}
"""


with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message.encode("utf-8"))

## para rodar esse codigo, deixar rodando em um terminal:
# python -m smtpd -c DebuggingServer -n localhost:8025 ## é importante ESPECIFICAR o encode, para caso exista acentos e etc.
# de outro terminal, enviar a mensagem, que o recebimento é simulado

## para enviar emails com google e etc: with smtp#lib.SMTP("smtp.mailtrap.io", 2525) as server:
#    server.login(user="83f1618af77272", password#="ff77c56ae6ef22")
#    server.sendmail(FROM, TO, message.as_string(#))
