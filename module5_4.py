with open('test4.txt', 'r', encoding='UTF-8') as f:
  old_data = f.read()

new_data = old_data.replace('One', 'Один').replace('Two', 'Два').replace('Three', 'Три').replace('Four', 'Четыре')
with open('test4_1.txt', 'x+', encoding='UTF-8') as new_f:
  new_f.write(new_data)