#!/usr/bin/env python3

# Abstração e Herança com dataclasse?

# from abc import ABC, abstractmethod
#
#
# class Instrument(ABC):
#
# @abstractmethod
# # usando o decorator que não deixa instâncias de classe abstrata serem criadas
# def play(self):
# ...
#
#
# class Guitar(Instrument):
# sound: str = "Ding Ding Ding"
#
# # quando o decorator abstractmethod é usado na classe base, os métodos que ele decora precisam ser usados nas classes concretas (ou seja, as que herdam o que a classe base tem)
# def play(self):
# return self.sound
#
#
# class Flute(Instrument):
# sound: str = "Flu Flu Flu"
# # caso exista um abstractmethod em uma classe base e a classe concreta não tenha o método implementado, dá erro. Precisa adicionar o que está comentado abaixo na classe Flute.
# # def play(self):
# # return self.sound

### usando herança COM dataclass

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import List


# Enum / Enumeração
class InstrumentKind(str, Enum):
    # fazendo uma enumeração a partir da classe base Enum
    # trabalha com ints, a partir do 0 se não tiver sido usado strna assinatura da funcao
    # ainda que sejam usadas palavras ao inves de int, o "peso" de cada atributo estará de acordo com o número (string será menr que wind 0 < 1).
    string = "string"
    wind = "wind"
    keys = "keys"
    drums = "drums"


class Distortion(str, Enum):
    wave = "wave"
    whisper = "whisper"


class ABCInstrument(ABC):

    @abstractmethod
    def play(self):
        ...


@dataclass
class DataInstrumentMixin:
    # mixin é uma classe que serve apara ser usada com o utra
    name: str
    sound: str
    # kind: str sem usar enum, os nomes seriam digitados
    kind: InstrumentKind  # usando o que foi especificado usando enum
    colors: List[str] = field(
        default_factory=list
    )  # iniciando atributo com valor default em usando o dataclass


class Instrument(DataInstrumentMixin, ABCInstrument):
    # a classe instrument herda coisas da mixin (pode ter mais de uma) e da classe base onde tem o abstractmethod
    ...


@dataclass
class Guitar(Instrument):
    sound: str = "Ding Ding Ding"
    #kind: str = "string"
    kind: InstrumentKind = InstrumentKind.string
    colors: List[str] = field(default_factory=lambda: ["green", "black"])

    def play(self):
        return self.sound


@dataclass
class ElectricGuitar(Guitar):  # herda de Guitar
    sound: str = "Wah Wah Wah"

    def play(self, distortion=Distortion.wave):
        return_from_baseclass = super().play()
        # super() serve para ser possível sobrescrever o método de uma classe (chamando o método da classe base) (usa um negócio chamado mro, ou method resolution order)
        if distortion is Distortion.wave:
            return "~~~".join(return_from_baseclass.split())
        elif distortion is Distortion.whisper:
            return "...".join(return_from_baseclass.split())
        return return_from_baseclass


@dataclass
class Flute(Instrument):
    sound: str = "Flu Flu Flu"
    # kind: str = "wind"
    kind: InstrumentKind = InstrumentKind.wind
    colors: List[str] = field(default_factory=lambda: ["silver", "black"])

    def play(self):
        return self.sound


# Tem enum no Python?
# ENUM / ENUMERAÇÃO

# dataclasses com valor default dão erro.
# para que serve o super()?
