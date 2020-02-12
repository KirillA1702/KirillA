user_input = input('Введите строку: ')
user_inputs = user_input.split()
for i, value in enumerate(user_inputs):
    print(i+1, value[:10])