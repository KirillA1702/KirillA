def to_int(user_input):
    if user_input.isdigit():
        return int(user_input)
    return 0

user_typing = True
result = 0
while user_typing:
    user_input = input("Введите последовательность строк через пробел:")
    index_input = user_input.find('_')
    if index_input != -1:
        user_input = user_input[:index_input]
        user_typing = False
    result += sum(map(to_int, user_input.strip().split(' ')))
    print(result)