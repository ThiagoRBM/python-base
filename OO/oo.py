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
