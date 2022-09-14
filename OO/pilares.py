#!usr/bin/env python3

## Abstração: representar um objeto do mundo real.


class Person:  # classe abstrata (objeto geenralizado, não se refere a uma pessoa específica)
    """Represents a Person"""
    kingdom = "animalia"


class Fruit:
    """Represents a fruit"""
    kingdom = "Plantae"


class Animal:
    """Represents an animal"""
    kingdom = "animalia"


## Herança


class Fruit:  # Classe abstrata
    kingdom = "Plantaes"


class Apple(Fruit):  # Classe Material 'Fruit' é de onde veio a herança
    colors = ["red", "white"]
    image = "🍎"


class Watermelon(Fruit):
    colors = ["green", "red"]
    image = "🍉"


class Pineapple(Fruit):
    colors = ["yellow", "green"]
    image = "🍍"


for fruit in [Apple(), Watermelon(), Pineapple()]:
    print(fruit.image, fruit.kingdom, fruit.colors)

## uma classe pode não ter nada dentro, com tudo sendo herdade de classes anteriores.

from abc import ABC
# ABC de Abstract Base Class


class Fruit(ABC):
    kingdom = "vegetalia"


## Polimorfismo
# "valor" in objeto  # objeto pode ser qualquer tipo que implementa `__contains__`


class Dog:

    def make_sound(self):
        return "woof woof"


class Cat:

    def make_sound(self):
        return "meow meow"


class Bird:

    def make_sound(self):
        return "pew pew"


def print_sound(obj):  # objeto "soundable"
    print(obj.make_sound())  # implementa make_sound


print_sound(Dog(
))  # a funcao não se importa com o tipo do objeto (gato, cachorro, etc)
print_sound(Cat())
print_sound(Bird())

## Encapsulamento. Capacidade de um objeto esconder sua implementação interna e expor apenas o que for conveninente. Tem estratégias para isso. Uma delas é a "convenção de nomes". Atributo iniciando com um anderline. Ele só pode ser acessado dentro da classe. Não dá para usar fora da classe (e.g. print(Conta._tipo_de_conta))
## Com DOIS underlines no começo, ele passa a ser privado e nem aparece com o dir(classe).


class Conta:
    _tipo_de_conta = "corrente"
    __id_interno = 985645

    def __init__(self, cliente):
        self.cliente = cliente
        self._saldo = 0

    def depositar(self, value):
        self._saldo += value

    def sacar(self, value):
        self._saldo -= value
        return value

    def consultar(self):
        if self._saldo < 0:
            print("AVISO: Você está devendo")
        return self._saldo


conta = Conta(cliente="Bruno")
print(dir(conta))
# Privado via name mangling
# Não é possível acessar `conta.__id_interno` mas por conta e risco:
'_Conta__id_interno',

# Protegido por convenção de nome:
# É possível acessar `conta._saldo` mas o `_` denota que esse valor
# deve ser acessado apenas internamente dentro dos métodos da própria classe.
'_saldo',
'_tipo_de_conta',

# Atributos e métodos públicos
'cliente',
'consultar',
'depositar',
'sacar'

conta = Conta(cliente="Bruno")
conta.depositar(100)
conta.sacar(10)
print(conta.consultar())
print(conta.cliente)
