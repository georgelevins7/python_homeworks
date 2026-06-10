# # BMI

w = float (input ("Please enter your weight: "))
h = float (input ("Please enter your height: "))

BMI = w / h**2

if BMI < 19:

    print ("underweight")

elif 19 <= BMI <=25:

    print ("normalweight")

elif BMI > 25:

    print ("overweight")







# კალკულატორი

a = int (input ("Enter first number: "))
b = int (input ("Enter second number: "))
c = input ("Enter operator: ")

if c == ("+") :
    print (a + b)
elif c == ("-") :
    print (a - b)
elif c == ("*") :
    print (a * b)    
elif c == ("/") :
    print (a / b)
elif c == ("%") :
    print (a % b)
elif c == ("//") :
    print (a // b)
elif c == ("**") :
    print (a**b)







# ყველაზე დიდი რიცხვი

a = int (input ("შეიყვანეთ პირველი რიცხვი: "))
b = int (input ("შეიყვანეთ მეორე რიცხვი: "))
c = int (input ("შეიყვანეთ მესამე რიცხვი: "))

if a == b or a == c or b == c:
    print ("შეიყვანეთ განსხვავებული რიცხვები!")
    
elif a > b and a > c:
    print (a)

elif b > a and b > c:
    print (b)

elif c > b and c > a:
    print (c)