import random
nums = []; i = 0; x = int(input('Введите колличество чисел: '))
while i < x:
    nums.append(random.randint(0,10))
    i += 1
print(nums); print('=' * 50)
uniq_list = (x for x in nums if nums.count(x) == 1)
print(list(uniq_list))