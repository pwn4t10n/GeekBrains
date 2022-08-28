def my_func(x, y, z):
    a = [x, y, z]
    a.sort()
    return a[1] + a[2]


r = my_func(5, 19, 1)
print(r)


def my_func2(arg1, arg2, arg3):

    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3


r2 = my_func2(90, 156, 11)
print(r2)
