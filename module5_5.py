with open('test5.txt', 'w', encoding='UTF-8') as f:
    typing = 1
    while typing:
        str_int = input(': ')
        f.write(str_int + ' ')
        if str_int == ' ' or str_int == '':
            typing = False

with open('test5.txt', 'r+', encoding='UTF-8') as f:
    num = []
    lines = f.readlines()
    for line in lines:
        a = lines[0].split()
        for b in a:
            num.append(int(b))
    print(sum(num))
