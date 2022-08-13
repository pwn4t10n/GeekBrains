lst = input("Введите слова через пробел: ").split()
k = 1
for i in lst:
    if len(i) > 10:
        print(f"{k}.{i[:10]}")
    else:
        print(f"{k}.{i}")
    k+=1
