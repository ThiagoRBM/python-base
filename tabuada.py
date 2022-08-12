#!/usr/bin/env python3

__version__ = "0.1.1"
__author__ = "Thiago"

seq=range(1,11)

for i in seq:
	#print(f"{'-'*4} Tabuada do {i} {'-'*4}\n")
	print("{:-^25}".format(f"Tabuada do {i}"))
	for x in seq:
		print("{:^25}".format(f"{i:03d} x {x:03d} = {i*x:03d}"))
	print("#" * 25 + "\n")
