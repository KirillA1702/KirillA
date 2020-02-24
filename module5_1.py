lines = ['first', 'second', ' ', 'third']
with open('test1.txt', 'w') as f:
    for line in lines:
        f.write(line + '\n')
        if line == ' ':
            break