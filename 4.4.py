
a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

b = []
[b.append(x) for x in a if x not in b]

print (b)


