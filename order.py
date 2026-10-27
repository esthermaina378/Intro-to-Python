ages = [21, 72, 56, 18, 19, 20, 31,48]

names = ["Esther", "Jimmy", "Francis", "Alicia", "Josey", "David", "John"]
# functions
ages.append(31)
# ages.clear
# ages.sort()
# ages.reverse()
print(ages)

names.sort()
print(names)

names.count("Francis")
print(names.count("Francis"))

print(len(names))
print(len(ages))

print(sum(ages)/len(ages))

# Retrieve an element
print(ages[0])
print(ages[6])
# For -1 you count from the end
print(ages[-2])

print(names[-3:]) #slicing (from end the 3 will display)
print(ages[-3:])
print(ages[3:5]) #slicing list

# set- removes duplicates
scores = {36, 90, 17, 89, 90}
print(scores)
scores.add(70)
print(scores)

# tuple - cannot be modified
weekdays = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
print(weekdays[5])

# dictionary
person = {"name": "Esther", "age": 20, "job": "Digital Forensics Analyst"}
print(person["name"])
print(person["age"])

print(person["job"])
people = [{"name": "John", "age":29},
          {"name": "Jimmy", "age":27},
          {"name": "Francis", "age":63},
          ]

print(people[2]["name"])