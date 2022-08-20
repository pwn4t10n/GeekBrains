def sum():
    r = 0
    ex = False
    while ex == False:
        number = input('Введите число или Q для выхода: ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        r = r + res
        print(f'Нынешняя сумма — {r}')
    print(f'Конечный результат — {r}')


sum()