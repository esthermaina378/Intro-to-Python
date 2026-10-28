import math


def greet():
    print("Hello")

def greeting(name):
    print(f"Hello {name}")

def volume_cylinder(radius, height):
     v = 22/7 * radius**2 * height
     print(round(v,2))

def volume_cylinder2(radius, height):
    v = 22/7 * radius**2 * height
    return v

def volume_surface(radius, height):
    v = 22/7 * radius**2 * height
    a = 22/7 * radius**2 * 2 + 22/7 * radius*2 * height
    return v, a




# greet() #calling a function/ no arguments or parameters

# greeting("Silah")
# greeting("Maina")
# greeting("Esther")

# volume_cylinder(radius=5, height=10)
# result = volume_cylinder2(radius=10, height=21)
# print(result)
#
# with open("volumes.txt", "w") as file:
#     file.write(str(result)

volume, area = volume_surface(radius=10, height=20)
print(f"Volume is {volume} and Area is {area}")


# name parameters
v,a = volume_surface(height=10, radius=20)
print(f"Volume is {v} and Area is {a}")

def divide(x, y, should_round: bool=False):
    res= x / y
    if should_round== True:
        return round(res,2 )
    else:
        return res
print(divide(1, 2, should_round=True))