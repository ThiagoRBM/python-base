#!/usr/bin/env python3

# tudo o que implementa o protocolo __str__ é "printable".
dados = [1, {"key": "value¨"}, True]
print(dados)
print(dir(dados))

dados = int
print(dados)  # aparece <class 'int'>
# protocolo __repr__ (representacao do objeto)

## protocolo printable padrão:


class Cor:
    icon = "⬜"


class Amarelo(Cor):
    icon = "🟨"


class Azul(Cor):
    icon = "🟦"


class Vermelho(Cor):
    icon = "🟥"


print("Cores primárias")
print(Amarelo())  # imprime a representação (__repr__)
print(Azul())
print(Vermelho())

## customizando o procotolo:


class Cor:
    icon = "⬜"

    def __str__(self):
        return self.icon


class Amarelo(Cor):
    icon = "🟨"


class Azul(Cor):
    icon = "🟦"


class Vermelho(Cor):
    icon = "🟥"


print("Cores primárias")
print(Amarelo())
print(Azul())
print(Vermelho())

### PROTOCOLO ADDIBLE
## protocolos __add__ (atua no objeto que está na esquerda) e __radd__ (atua no objeto que está na direita)


class Cor:

    def __str__(self):
        return self.icon

    def __add__(self, other):
        # definiu o protocolo __add__ que não existe na classe "cor" (que não é padrão do python).
        mixtable = [
            ((Amarelo, Vermelho), Laranja),
            ((Azul, Amarelo), Verde),
            ((Vermelho, Azul), Violeta),
        ]
        for mix, result in mixtable:
            if isinstance(self, mix) and isinstance(other, mix):
                # isinstance é uma funcao padrao do python que verifica se um objeto é uma instância de uma classe.
                return result()


class Amarelo(Cor):
    icon = "🟨"


class Azul(Cor):
    icon = "🟦"


class Vermelho(Cor):
    icon = "🟥"


class Laranja(Cor):
    icon = "🟧"


class Verde(Cor):
    icon = "🟩"


class Violeta(Cor):
    icon = "🟪"


print("Cores secundárias")
print(Amarelo() + Vermelho())
print(Azul() + Amarelo())
print(Vermelho() + Azul())

## PROTOCOLO ITERABLE: __iter__


class Paleta:

    def __init__(self, *cores):
        self._cores = cores

    def __iter__(self):
        return iter([cor.icon for cor in self._cores])
        # iter é uma função padrão do pytho que consome iterável.


print("rgb")
rgb = Paleta(Vermelho(), Verde(), Azul())
for cor in rgb:
    print(cor, end="")

## PROTOCOLO CONTAINER: __contains__
# verifica se existe uma instância dentro de uma classe. Retorna bool.
# lista, sets, dicionários, tudo isso implementa esse protocolo.


class Paleta:

    def __init__(self, *cores):
        self._cores = cores

    def __contains__(self, item):
        return item in [cor.icon for cor in self._cores]


print("red in rgb?")
rgb = Paleta(Vermelho(), Verde(), Azul())
print("🟥" in rgb)

## SIZED: __len__
# objetos que implementes esse protocolo podem ser passados para a função len


class Paleta:

    def __init__(self, *cores):
        self._cores = cores

    def __len__(self):
        return len(self._cores)


print("rgb size")
rgb = Paleta(Vermelho(), Verde(), Azul())
print(len(rgb))

## PROTOCOLO COLLECTION:
## "superprotocolo", mistura objetos que tem protocolos : __contains__ , __iter__ , __len__
# container, iterable e sized
# pode fazer qualquer coisa dos protocolos acima.


class Paleta:
    # exemplo de colletcion
    def __init__(self, *cores):
        self._cores = cores

    def __len__(self):
        return len(self._cores)

    def __contains__(self, item):
        return item in [cor.icon for cor in self._cores]

    def __iter__(self):
        return iter([cor.icon for cor in self._cores])


## PROTOCOLO SUBSCRIPTABLE: __getitem__


class Paleta:

    def __init__(self, *cores):
        self._cores = cores

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            # se o que foi pedido for um item ou "fatia" (0 ou 1:2)
            return self._cores[item]
        elif isinstance(item, str):
            for cor in self._cores:
                if cor.__class__.__name__.lower() == item.lower():
                    # se receber uma string (nome), vai transformar o nome da classe para minúsculo e compara com a string recebida
                    return cor


rgb = Paleta(Vermelho(), Verde(), Azul())
print(rgb[0])
print(rgb["azul"])
print(rgb[1:])

# Classes criadas vazia já vem por padrão com vários protocolos. Esses protocolos são herdados da classe object. (dir(object)):

print(dir(object))


class Thing:
    ...


thing = Thing()
print(thing)  # __repr__ Representable
thing == 1  # __eq__ Equality Comparable

print(f"aa:   {dir(thing)}")
'''
__new__  # Construtor chamado antes de criar a intância
__init__  # Inicializador chamado após a instância é criada
__init_subclass__  # Inicializador de subclasses
__repr__  # Imprime a representação em string
__str__  # chama __repr__ por padrão
__setattr__  # executado sempre que atribuimos com obj.name = value
__getattr__  # executado quando acessamos obj.name
__delattr__  # executado quando apagamos com `del obj.name`
__getattribute__  # executado quando um atributo não é encontrado
__dir__  # lista todos os atributos e métodos
'''
