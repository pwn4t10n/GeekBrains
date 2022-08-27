lst = [1, False, 'Привет', 1.08]
k = 1
for i in lst:
    t = type(i)
    print(f"{k}-ый элемент списка относится к типу {t} ")
    k+=1