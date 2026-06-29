# ტრანზაქციის ფუნქცია

def comission(func):
    def inner(balance, awc):
        comission = 1
        amount = awc + comission
        if amount > balance:
            return "Not enough money!"
        
        return func(balance, amount)
    return inner

@comission
def transaction(balance, awc):
    return balance - awc

print(transaction(44,44))


# დეკორატორი count_calls

count = 0

def count_calls(func):
    def inner():
        global count
        count += 1
        func()
    return inner

@count_calls
def base():
    return(base)

base()
base()
base()

print(count)