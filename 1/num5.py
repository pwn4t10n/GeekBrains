print('Введите выручку: ')
rvn = int(input())
print('Введите издержки')
csts = int(input())
if rvn > csts:
    print('Прибыль')
elif rvn < csts:
    print('Убыток')