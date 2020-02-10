rating = [7, 5, 3, 3, 2]
user_input = int(input('Введите элемент рэйтинга: '))
for x in rating:
    if x == user_input:
        i = rating.index(x)
        rating.insert(i, user_input)
        break
    elif x < user_input:
        rating.insert(0, user_input)
        break
else:
    rating.append(user_input)

print(rating)