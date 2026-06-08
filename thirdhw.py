# პირველი სიტყვის ჩანაცვლება მეორეთი

text = (input ("შეიყვანეთ წინადადება: "))
f_sent = (input ("შეიყვანეთ პირველი სიტყვა: "))
s_sent = (input ("შეიყვანეთ მეორე სიტყვა: "))
print (text.replace(f_sent, s_sent))


# ყველაზე გრძელი სიტყვა

text = input ("შეიყვანეთ ტექსტი: ")
# ("Tbilisi is the capital of Georgiaa")

tl = (text.split())

print (len(tl[0])) # უბრალოდ დავპრინტე, შემდგომ რა მექნა ვერ მოვიფიქრე

# ანაგრამა

word1 = input("შეიყვანეთ პირველი სიტყვა: ")
word2 = input("შეიყვანეთ მეორე სიტყვა: ")
w1 = word1.lower()
w2 = word2.lower()

print(w1,w2) #საჭირო არ იყო