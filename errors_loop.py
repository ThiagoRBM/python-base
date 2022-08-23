#!/usr/bin/env python3
import time
import logging

log = logging.Logger("errors")

# EAFP - Easy to ASk Forgiveness than permission
# (É mais fácil pedir perdão do que permissão)


def try_to_open_a_file(filepath, retry=1):
    for attempt in range(1, retry + 1):
        print(f"tentativa número {attempt}")
        try:
            return open(filepath).readline()
        except FileNotFoundError as e:
            log.error("ERRO %s", e)
            time.sleep(2)  
            # ^ isso aqui é só para fingir que estamos esperando um processo terminar
        else:
            print("Sucesso!!!")
        finally:
            print("Execute isso sempre!")
    return []


for line in try_to_open_a_file("names.txt", retry=5):
    print(line)
