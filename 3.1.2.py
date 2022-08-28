def div(f, s):
    try:
        return f/s
    except ZeroDivisionError:
        return "Деление на 0 невозможно"


r = div(5, 0)
print(r)
