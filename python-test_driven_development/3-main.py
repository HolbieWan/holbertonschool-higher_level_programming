#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name(("", "John"))
try:
    say_my_name("Momo", 444)
except Exception as e:
    print(e)
