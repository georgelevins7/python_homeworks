# ფაქტორიალი

num = int(input("Enter number: "))

z = 1

for w in range(num, 0, -1):
    z *= w

print(z)

# # გამრავლების ტაბულა

for a in range(1, 10):
    for k in range (1, 10):
        print (f"{a} * {k} =", a * k)

# აპარატი

amount = 50

while amount > 0:
    num = int(input("Pay: "))

    if num != 5 and num != 10 and num != 20:
        print (f"Not valid amount! You have to pay {amount} GEL!")
        continue
    amount -= num

    if amount > 0:
        print (f"You have to pay {amount} GEL!")
    elif amount == 0:
        print ("Payment completed!")
    else:
        print("Payment completed!")
        print(f"Your change is {-amount} GEL")