a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
b = [a[i+1] for i in range(len(a)-1) if (a[i+1] > a[i])]
print(b)
