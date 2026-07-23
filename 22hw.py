import threading

num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51]
threads = []
results = []

def simple(num):
    global results
    if num == 0 or num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            results.append((num, False))
            return False
    results.append((num, True))
    return True


for i in num_list:
    t = threading.Thread(target=simple, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(results)