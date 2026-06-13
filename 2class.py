import random

num1 = random.randint(1, 100)
l = 5

while l > 0:
    num2 = int(input ("enter number: "))
    if num2 == num1:
        print ("You win!")
        break
    elif num2 < num1:
        l -= 1
        print ("number is much!")
        print (f"lives: {l}")
    else:
        l -= 1
        print ("number is less!")
        print (f"lives: {l}")

if l == 0:
    print ("You lose!")



# if num1 == num1:
#     print ("You win!")
# else:
#     print (num2-num1) or (num1-num2)