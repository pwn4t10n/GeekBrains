def sum(x,y,z):
    a = [x,y,z]
    a.sort()
    return a[1] + a[2]
r = sum(5, 19, 1)
print(r)