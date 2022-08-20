from itertools import count, cycle

for i in count(3):
    if i > 10:
        break
    else:
        print(i)


с = 0
for x in cycle("ABC"):
    if с > 11:
        break
    print(x)
    с += 1