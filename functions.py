# functions and methods
# print("Hello World") # built in function
from custom_functions import greet

with open("temp.txt", "w") as file:
    file.write("76.5\n")
    file.write("99.5\n")
    file.write("54.35\n")
with open("temp.txt", "r") as file:
     content = file.read()
     print(content)

     # pip install yt-dlp
