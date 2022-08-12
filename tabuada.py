#!/usr/bin/env python3

seq=range(1,11)

for i in seq:
	print("-"*3 + "Tabuada do " + str(i) + "-"*3)
	for x in seq:
		print("{:^19}".format(f"{i:03d} x {x:03d} = {i*x:03d}"))
	print("#" * 19)
	print("\n")
