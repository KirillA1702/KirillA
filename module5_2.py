count = 0
with open('test2.txt', 'r') as f:
    for line in f:
        count += 1
    print(count)

with open('test2.txt', 'r') as f:
    lines = f.readlines()
    for i, word in enumerate(lines):
        num_words = len(word.split())
        print(f'Линия {i + 1} имеет {num_words} слова')