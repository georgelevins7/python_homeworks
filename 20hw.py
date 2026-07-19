class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: ({self.name}, {self.age})"

p1 = Person("Otar", 35)

def serializer(person):
    return f"Name: {person.name}, Age: {person.age}"

def deserializer(data):
    lst = data.split(", ")
    name = lst[0].split(": ")
    age = lst[1].split(": ")
    return Person(name[1], int(age[1]))

with open("per.txt", "w") as file:
    file.write(serializer(p1))
with open("per.txt", "r") as file:
    data = file.read()

deser = deserializer(data)

print(deser)

import json

with open("persons.json", "r") as file:
    persons = json.load(file)

last_id = persons[-1]["id"]

def adding(number):
    global last_id
    while number > 0:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        number -= 1
        last_id += 1
        dct = {
            "id": last_id,
            "name": name,
            "age": age
        }
        persons.append(dct)

adding(2)

with open("persons.json", "w") as newfile:
    json.dump(persons, newfile, indent=4)