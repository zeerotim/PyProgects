def my_func(x:float, y:int):
    if x == 0:
        return 0
    result = 1
    if y > 0:
        for i in range(y):
            result *= x
    elif y < 0:
        for i in range(abs(y)):
            result = result/x
    return result

print(my_func(2, 0))


