def my_func1(x:float, y:int):
    result = x**y
    return result

def my_func2(x:float, y:int):
    if x == 0 and y != 0:
        return 0
    result = 1
    if y > 0:
        for i in range(y):
            result *= x
    elif y < 0:
        for i in range(abs(y)):
            result = result/x
    return result

print(my_func1(0, 0))

print(my_func2(0, 0))
