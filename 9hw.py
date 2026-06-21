# მაღალ რეგისტრში გადაქცევა

def upp(text):

    cnt = 0
    for sym in text:
        if sym.isupper():
            cnt += 1
    print(cnt)
    print(text.upper())

text = input("Enter text: ")
upp(text)

# camel snake cases

def snake(camel):

    sn_txt = ""
    for sym in camel:
        if sym.islower():
            sn_txt += sym
        if sym.isupper():
            sn_txt += f"_{sym.lower()}"
    return sn_txt

camel = input("Camel case: ")
print(snake(camel))