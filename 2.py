lst = input('Введите целые числа через пробел:').split(' ')
f = 0
s = 1
while len(lst) > s:
    lst[f], lst[s] = lst[s], lst[f]
    f += 2
    s += 2
print(lst)