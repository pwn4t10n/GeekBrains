lst = [6, 10, 3, 2, 2]
while True:
    a = input("Введите оценку от 1 до 10 или введите '0' для выхода: ")
    if a != '0':
        lst.append(int(a))
        lst.sort(reverse=True)
        print(lst)
    else:
        break
        