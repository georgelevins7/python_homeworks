# დიქტი კვადრატებით
dct = {key:key ** 2 for key in range(1,11)}

print(dct)


# პროდუკტების სია

products = [
    {"cola": {
        "price": 1.5,
        "quantity": 10
    }},
    {"fanta": {
        "price": 2.5,
        "quantity": 5
    }},
    {"snickers": {
        "price": 3.5,
        "quantity": 12
    }},
    {"water": {
        "price": 4.5,
        "quantity": 8
    }},
    {"beer": {
        "price": 6.5,
        "quantity": 5
    }}
]

for key in products:
    for name in key:
        print(name)



z = 0
for lst in products:
    for name in lst:
        z += (lst[name]["price"]) * (lst[name]["quantity"])
            
print(z)


# ხილის რაოდენობის დიქტი

fr_dict = {}


while True:

    fruit = input("Enter fruit: ")
    if fruit == "stop":
        print(fr_dict)
        break
    elif fruit not in fr_dict:
        fr_dict.update({fruit:1})
    else:
        fr_dict.update({fruit:fr_dict[fruit]+1})