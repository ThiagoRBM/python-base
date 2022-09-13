#!/usr/bin/env python3

people = [{
    "name": "Jim Halpert",
    "balance": 500,
    "role": "Salesman"
}, {
    "name": "Dwight Schrute",
    "balance": 100,
    "role": "Manager"
}]


def add_points(person, value):
    #  funcao "impura"
    if person["role"] == "manager":
        value *= 2
    person["balance"] += value
    return person


# declarativo:
for person in people:
    add_points(person, 100)

print(people)

# funcional "impuro":
map(lambda person: add_points(person, 100),
    people)  # inicialmente o objeto não é criado (lazy evaluation)

resultado = map(lambda person: add_points(person, 100),
                people)  # agora ele vai ser criado

print(list(resultado))

# funcional "puro":


def add_points(person, value):
    data = person.copy(
    )  # copiamos o valor de entrada ao invés de altera-lo (em programação funcional "pura", se evita criação de side effects, e alteração dos objetos que funçẽos recebem)
    if data["role"] == "manager":
        value *= 2
    data["balance"] += value
    return data


result = map(lambda person: add_points(person, 100), people)
print("Resultado funcional:", list(result))
print("Dados originais sem side effects:", people)

## ORIENTACAO A OBJETOS


# Definição da classe
# pascalCase ou UpperCamelCase é a convenção de nomenclatura .Em caso de SIGLAS, colocar tudo em maiúsculo
class Person:
    """Represents a Person"""

    # Atributos da classe
    name = "Jim Halpert"
    role = "Salesman"
    balance = 100

    # Métodos ou funções associadas
    def add_points(person, value):
        if person.role == "manager":
            value *= 2
        person.balance += value


jim = Person()  # Instanciação de um objeto a partir da classe

jim.add_points(500)  # Chamada de método associado

print(jim.balance)  # Acesso a atributo

print(Person.__dict__)  # a implementação da classe é um dicionário.

pessoa1 = Person()
pessoa2 = Person()

print(pessoa1.name)
print(
    pessoa1.__dict__
)  # as características da instância também tem os dados armazenados em um dicionário.
print(pessoa2.name)


# criacao de classes vazias
class Obj:
    ...


class Obj:
    pass
