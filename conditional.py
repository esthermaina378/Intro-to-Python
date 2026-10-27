# if else
import os

name = input("What is your name?" )
age = input("What is your age?")

if not age.isnumeric():
    print("Invalid age")
    os._exit(0)

if int(age) > 18:

    print(name+" is an Adult")

else:
    print(name+" ia a Child")