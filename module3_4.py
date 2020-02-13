def my_func(x, y):
    return x ** y

print(my_func(float(input('x: ')), int(input('y: '))))

def my_func(x, y):
    result = 1
    while y < 0:
        result /= x
        y += 1
    print(result)
my_func(float(input('x: ')), int(input('y: ')))