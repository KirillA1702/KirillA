# file = open('file.txt')
# line = file.readline().strip()
# print(line)
# line = file.readline().strip()
# print(line)
# line = file.readline().strip()
# print(line)

# f = open('file.txt', 'w')
# # f.write('kjdgsfkjs')
# f.writelines(['qwe', 'rtyrty', 'qweqw'])
# f.close()
# print(f)

# with open('2341.txt', 'w') as f:
#     f.writelines(['qwe', 'rty'])
#     print(f.closed)
#     print(f.mode)
#     print(f.name)

# try:
#     f_obj = open('file.txt')
#     for line in f_obj:
#         print(line)
# except IOError:
#     print('Ошибка')
# finally:
#     f_obj.close()

# with open('2341.txt', 'w+') as f_obj:
#     f_obj.write('qwe\nrty\ncvb')
#     f_obj.seek(0)
#     print(f_obj.read())

# import os
# os.remove('file.txt')

import json

# data = {'income': {'salary': 5000, 'bonus': 1000}}
# # with open('data.json', 'w') as f:
# #     json.dump(data, f)
# #
# # with open('data.json') as f:
# #     data1 = json.load(f)
# # print(data1)
# # print(type(data1))
# js = json.dumps(data)  #str
# js1 = json.loads(js)  # как есть, как dict
# print(js1)
# print(js)

import shutil
shutil.copy()
shutil.copyfile()
shutil.rmtree()
shutil.move()