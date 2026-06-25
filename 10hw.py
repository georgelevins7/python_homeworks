# 5 რიცხვის ჯამი
def num(a = 5):
    sum = 0
    for i in range(a):
        number = int(input("Enter number: "))
        sum += number
    return sum

print(num(2))


# კენტი ლუწი

def main(*args):
    lst1 = []
    lst2 = []
    for num in args:
        if num % 2 == 0:
            lst2.append(num)
        else:
            lst1.append(num)
    return lst1, lst2
print(main(1,2,4,6,8,10))


# წინადადებაში სიტყვების დათვლა

def main(sent):
    dct = {}
    sent = sent.lower()
    sent = sent.replace(".", "")
    sent = sent.replace(",", "")
    sent = sent.replace("!", "")
    sent = sent.replace("?", "")
    sent = sent.replace(":", "")
    sent = sent.replace(";", "")
    sent = sent.split()
    for word in sent:
        if word not in dct:
            dct.update({word: 1})
        else:
            dct.update({word:dct[word]+1})
    return dct
sent = input("Enter sentence: ")
print(main(sent))

# პროდუქტების სია

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 15},
    {"name": "Keyboard", "price": 25},
    {"name": "Monitor", "price": 150},
    {"name": "Power", "price": 100},
    {"name": "Pad", "price": 10},
]

pr = filter(lambda x: x["price"] < 100, products)
print(list(pr))

mp = map(lambda d: (d["name"], d["price"]), products)
print(list(mp))

so = sorted(products, key=lambda t: t["price"])
print(so)

from functools import reduce

rd = reduce(lambda u, q: u + q["price"], products, 0)
print(rd)

# რეკურსია

def rec(a):
    if a == 1:
        return 1
    return a + rec(a-1)

print(rec(5))