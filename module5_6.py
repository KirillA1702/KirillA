import json
import re

subject_dict_with_time = []

with open('test6.txt', encoding='UTF-8') as read_file:
    open_obj = read_file.readlines()
    for pr in open_obj:
        subject_dict = pr.split()
        subject = subject_dict[0]
        all_time = sum([int(subject_time) for subject_time in re.findall(r'\d+', pr)])
        subject_dict_with_time.append({subject: all_time})

with open('data_file.json', 'w', encoding='UTF-8') as write_file:
    json.dump(subject_dict_with_time, write_file)
print(subject_dict_with_time)