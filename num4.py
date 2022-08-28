print('Введите число: ')
a = int(input())
dig = 0
while a > 10:
    dv = a % 10
    a //= 10
    if dv > dig:
        dig = dv
print(f"Самое большое число: {dig}")