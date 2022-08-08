print('Введите выручку: ')
rvn = int(input())
print('Введите издержки')
csts = int(input())
res = str
if rvn > csts:
    res = 'прибыль'
elif rvn < csts:
    res = 'убыток'
rent = int
if res == 'прибыль':
    rent = rvn / csts
    print(rent)
print('Введите число сотрудников: ')
qnt = int(input())
print(f"Прибыль в расчёте на одного сотрудника: {rvn//qnt}")
