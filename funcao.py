#!/usr/bin/env python3

names= ["Bruno","Joao","Bernardo","Barbara","Brian"]

def comeca_b(lista,inicial):
    """Retorna os elementos que começam com a letra espcificada.
    """
    for item in lista:
        if item[0].lower() == inicial:
            print(item)
        
comeca_b(names,"j")

######

vals=(2,5)
vals1=[2,5]
vals2= {"a":2,"b":5}

def soma(a,b):
	return a + b

soma(vals[0],vals[1])
soma(*vals)
soma(*vals1)
soma(**vals2)
