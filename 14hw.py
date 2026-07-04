# სახელი გვარი

file = open("names.txt", "w")
c = 1
while True:
    name = input("Enter your first name: ")
    if name == "stop":
        break
    file.write(f"{c}. ")
    file.write(f"{name}")
    file.write(" ")
    surname = input("Enter your last name: ")
    if surname == "stop":
        break
    file.write(f"{surname}")
    file.write("\n")
    c += 1

file.close()


# ორი სია ასაკით გაფილტრული

with open("persons.txt", "r") as file:
    for lines in file:
        ages = int(lines.split(",")[1])
        if ages < 50:
            with open("under50.txt", "a") as under:
                under.write(lines)
        if ages >= 50: # 1 ადამიანი არის 50 წლის, გადავწყვიტე ამ სიაში ჩამეგდო, რადგან 50 წელს აცდა
            with open("up50.txt", "a") as up:
                up.write(lines)


# ფუნქცია, csv-ში ჩაწერა

import csv


def quest(inputs):
    count = 1
    headers = ["ID", "first_name", "last_name", "age"]
    with open("persons.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        while inputs > 0:
            inname = input("Enter Your Name: ")
            insurname = input("Enter Your Surname: ")
            while True:
                try:
                    inage = int(input("Enter Your Age: "))
                    break
                except ValueError:
                    print("Enter only number!")

            person = {
            "ID": count,
            "first_name": inname,
            "last_name": insurname,
            "age": inage
            }
            writer.writerow(person)
            count += 1
            inputs -= 1

quest(2)


# passed და failed სტუდენტების სია

import csv

headers = ["ID", "First Name", "Last Name", "Grade"]
with open("students.csv", "r") as file:
    dict_reader = csv.DictReader(file)
    with open("passed_students.csv", "w") as passed:
        pswr = csv.DictWriter(passed, fieldnames=headers)
        pswr.writeheader()
        with open("failed_students.csv", "w") as failed:
            fawr = csv.DictWriter(failed, fieldnames=headers)
            fawr.writeheader()
        
            for lines in dict_reader:
                grades = int(lines["Grade"])
                if grades >= 50: # აქაც იყო 1 ადამიანი 50 ქულით, გადავწყვიტე ამ სიაში ჩამეგდო (სხვა შემთხვევაში მეორე if-ს ჩამოვწერდი)
                    pswr.writerow(lines)
                else: 
                    fawr.writerow(lines)