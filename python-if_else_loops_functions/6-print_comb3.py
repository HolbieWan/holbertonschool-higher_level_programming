#!/usr/bin/python3
for decimal in range(8):
    for units in range(decimal + 1, 10):
        print("{}{}" .format(decimal, units), end=", ")
print("89")
