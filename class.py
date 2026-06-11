try: 
    age = int(input("შეიყვანეთ ასაკი: "))
    if age < 0:
        raise ValueError("მნიშვნელობა უნდა იყოს დადებითი")
    
except ValueError:
    print("შეიყვანეთ მხოლოდ რიცხვი!")

else:
    if age < 18:
        print ("არასრულწლოვანი")
    else:
        print ("სრულწლოვანი")