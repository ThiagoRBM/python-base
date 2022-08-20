#!/usr/bin/env python3
""" Faça um programa que imprime os números pares de 1 a 200
"""

for n in range(1,201):
    if n % 2 ==0:
        print(n)

## com while
#n=0
#while n < 201:
#    n=n+1
#    if n % 2 ==0:
#        print(n)

## com list comprehension
#[print(n) for n in range(1,201) if n % 2 == 0]

