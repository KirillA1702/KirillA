def my_func(x, y, z):
    if x <= y <= z:
        return y + z
    elif y <= x <= z:
        return x + z
    elif z <= x <= y:
        return x + y
print(my_func(5,4,7))