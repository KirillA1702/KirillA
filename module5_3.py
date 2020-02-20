poor_employees = []
all_employees_salaries = []
with open('test3.txt', 'r', encoding='UTF-8') as f:
    for line in f.readlines():
        employee = line.split(' ')
        if float(employee[1]) < 20000:
            poor_employees.append(employee[0])
        all_employees_salaries.append(float(employee[1]))
avg_salary = sum(all_employees_salaries) / (float(len(all_employees_salaries)))
print(poor_employees)
print(round(avg_salary))