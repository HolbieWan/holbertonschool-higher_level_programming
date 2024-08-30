#!usr/bin/python3
def print_diagonal(n):
    for i in range(1, n + 1):
        print("\\")
        for j in range(0, i):
            print(" ", end="")

print_diagonal(5)