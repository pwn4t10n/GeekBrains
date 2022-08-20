import math
def fact(n):
    for i in range(n+1):
       yield i
a = fact(7)
for el in a:
    print(math.factorial(el))
