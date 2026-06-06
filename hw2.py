# ჰიპოტენუზა და ფართობი

cathet1 = int(input ("cathet1: "))
cathet2 = int(input ("cathet2: "))

print ("hypotenuse", ((cathet1**2+cathet2**2)**0.5))

print ("area", (cathet1*cathet2)/2)


# წამების რაოდენობა

a = int(input ("შეიყვანეთ წამების რაოდენობა: "))
h = a//3600
m = a%3600//60
s = ((a%3600)%60)
print (h, "საათი", m, "წუთი", s, "წამი")