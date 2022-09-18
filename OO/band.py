#!/usr/bin/env python3
"""Roda o que está no Script instruments.py"""

#ls band.py | entr -c -s "mypy band.py && ./band.py"

from instruments import Guitar, Flute, ElectricGuitar, InstrumentKind, Distortion

gianini = Guitar(
    "Giannini m2", kind=InstrumentKind.keys
)  # é possível mudar o tipo desde que o tipo do instrumento novo esteja listado na classe InstrumentKind
print(gianini.play())
print(gianini.colors)

digior = Guitar("m3", kind=InstrumentKind.string,
                sound="Nheim Nheim")  # é possível mudar o som
print(digior.play())
print(digior.colors)

lespaul = ElectricGuitar("Lespaul m1")
print(lespaul.play())

lespaul2 = ElectricGuitar("Lespaul m1")
print(lespaul.play(distortion=Distortion.whisper))

yamaha = Flute("Yamaha Magic Flute", colors=["silver"])
print(yamaha.play())
print(
    yamaha.colors
)  # por padrão seria uma lista vazia, mas foi alterada na assinatura da função
