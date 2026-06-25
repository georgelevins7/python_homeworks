from faker import Faker
import random

fake = Faker()

# print(fake.first_name())


def generate_student(stid: int) -> dict:
    dct = {
        "ID": stid,
        "fname": fake.first_name(),
        "sname": fake.last_name(),
        "age": random.randint(18,80)
    }
    return dct
print(generate_student(4))

def generate_students(a: int) -> list:
    lst = []

    for i in range (1, a + 1):
        lst.append(generate_student(i))

    return lst