#!/usr/bin/python3

tree_size = int (input("What is the size of the tree: "))

number_spaces = tree_size -1
number_hash = 3
tree_size_2 = tree_size

for f in range(0, tree_size -1):
    print(" ", end="")
print("#")

while (tree_size > 1):
    i = 1
    j = 0

    for i in range (0, number_spaces - 1):
        print(" ", end="")
    number_spaces -= 1
    
    for j in range (j, number_hash):
        print("#", end="")
    print("")
    number_hash += 2
    
    tree_size -= 1

for f in range(0, tree_size_2 - 1):
    print(" ", end="")
print("#")
