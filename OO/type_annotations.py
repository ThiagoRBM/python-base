#!/usr/bin/env python3

from decimal import Decimal

produto = "Caneta"
valor = Decimal(4.5)
quantidade = 5

#def calcula_total(valor, quantidade):
#    return valor * quantidade


## COM ANOTACAO DE TIPOS
## NÃO DÁ ERRO SE OS ARGUMENTOS NÃO ESTIVEREM DE ACORDO COM O ESPECIFIADO. A ferramenta mypy analisa se os tipos estão sendo seguidos.
# mypy type_annotations.py
def calcula_total(valor: Decimal, quantidade: int) -> Decimal:
    # implementando as type annotations (type hint)
    return valor * quantidade


total_da_compra = calcula_total(valor, quantidade)

total_da_compra = calcula_total(
    valor * Decimal(0.9), quantidade
)  # aqui dá erro porque apliquei um "desconto" de 10% mas usando float ao invés de decimal, que é o tipo requerido pela função. Se alterar para Decima(0.9), resolve.

print(f"A compra de {quantidade} {produto}s deu R$ {total_da_compra}")

## outras ferramentas ajudam a seguir as type annotations, uma é a beartype, que funciona com decorators. Em tempo de execução ela verifica os tipos.

## para rodar o arquivo sempre que salvar: ls type_annotations.py | entr -c -s "mypy type_annotations.py && ./type_annotations.py"

### COMPOSIÇÃO DE TIPOS
## dá para fazer várias coisas, como colocar argumentos opcionais e etc. Verificar documentação.
from typing import Union


# com union é possível aceitar mais de um tipo de argumento na função.
def calcula_total2(valor: Union[Decimal, int], quantidade: int) -> Decimal:
    return Decimal(valor * quantidade)


calcula_total2(1, 4)


## ao invés de importar Union, dá para fazer dessa forma (a partir do python 3.10):
def calcula_total3(valor: Decimal | int, quantidade: int) -> Decimal:
    return Decimal(valor * quantidade)


calcula_total3(1, 4)

## TYPE ALIAS. Quando a tipagem começar a ficar complexa, é possível criar uma estrutura (diferente de classe) de tipo.

from typing import Any, Tuple, List

## type_aliases.py
DictPessoa = dict[str, dict[
    str,
    Any]]  ## maneira antiga, dá para fazer direto usando os |, como falei acima.


def funcao(dados: DictPessoa):
    ...


# antes do Python 3.9
def function(arg: List[int] | Tuple[int]):
    ...


# após o Python 3.9
def function2(arg: list[int] | tuple[int]):
    ...


## é possível passar uma classe como tipo para uma função
class Pessoa:

    def __init__(self, pk: str, name: str, points: int):
        self.pk = pk
        self.name = name
        self.points = points


def funcao3(dados: Pessoa):  # usamos a própria classe para anotar
    ...


dados = Pessoa(pk="joe@doe.com", name="Joe", points=10)

funcao3(dados)

## DATACLASS: substitui o método __init__ para inicializar a classe.

from dataclasses import dataclass


@dataclass
class Pessoa2:
    pk: str
    name: str
    points: int


def funcao4(dados: Pessoa2):
    ...


dados3 = Pessoa2(pk="joe@doe.com", name="Joe", points=10)

funcao4(dados3)
