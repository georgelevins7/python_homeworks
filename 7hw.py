# ჯამი და საშუალო 

lst = [5, 12, 3, 39, 77, 100, 31, 27]

num = 0

for z in lst:
    num += z
print(num)
print(num / len(lst))

# უნიკალური ელემენტები

lst = ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1]
new_lst = []

for x in lst:
    if x not in new_lst:
        new_lst.append(x)

print (new_lst)


# რანდომ/ლუწი სიები

import random

lst = []
count = 20
new_lst = []

while count > 0:
    c = random.randint(-50, 50)
    lst.append(c)
    count -= 1

for x in lst:
    if x % 2 == 0:
        new_lst.append(x)

print (lst)
print (new_lst)

# სახელი, გვარი, ასაკი

persons = [
    ('Kelly', 'Simpson', 26),
    ('Erika', 'Stephens', 24),
    ('Cheryl', 'Dunn', 30),
    ('Amy', 'Larsen', 49),
    ('Christine', 'Gordon', 23),
    ('Monica', 'Huff', 38),
    ('David', 'Nixon', 36),
    ('Cindy', 'Escobar', 41),
    ('Cindy', 'White', 33), 
    ('Joel', 'Hall', 43),
    ('Steven', 'Winters', 28),
    ('Alex', 'Cole', 68),
    ('Alex', 'Smith', 32),
    ('Alex', 'White', 42),
    ('Brittany', 'Thompson', 18),
    ('Ernest', 'Young', 43),
    ('Traci', 'Wells', 38),
    ('Andrew', 'Flores', 61),
    ('Christopher', 'Lewis', 29),
    ('Kevin', 'Willis', 57),
    ('Kayla', 'Lucas', 28),
    ('Michelle', 'Rush', 43),
    ('Thomas', 'Mason', 37)
]


while True:
    n1 = input("Your Name: ")
    if n1 == "stop":
        break
    
    for x in persons:
        if x[0] == n1:
            s1 = input("Your Surname: ")
            if s1 == "stop":
                break

            for p in persons:
                if p[0] == n1 and p[1] == s1:
                    print (f"Age is {p[2]}")
                    break
            else:
                print("There is no such surname!")

            break
    else:
        print("There is no such name!")