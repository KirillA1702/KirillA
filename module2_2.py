nums = int(input('Введите длинну списка: '))
my_list = [num for num in range(nums)]
i = 0
while i < len(my_list) - 1:
    tmp = my_list[i]
    my_list[i] = my_list[i+1]
    my_list[i+1] = tmp
    i += 2
print(my_list)