try:
    num1 = float(input ("Enter Number1: "))
    num2 = float(input ("Enter Number2: "))
    c = num1 / num2

except ValueError:
    print ("Enter only number!")
except ZeroDivisionError:
    print ("You can't divide by zero!")
except Exception as d:
    print (f"Sorry, {d}")

else:
    print (f"{num1}/{num2}={c}")
finally:
    print ("End of programm.")