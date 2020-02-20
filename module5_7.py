''import json

firms = {}
profit_all = 0

with open('test7.txt', encoding='UTF-8') as read_file:
    open_obj = read_file.readlines()
    for pr in open_obj:
        firm_line = pr.split()
        firm_name = firm_line[0]
        profit_and_costs = [int(profit_or_costs) for profit_or_costs in pr.split() if profit_or_costs.isdigit()]
        profit = profit_and_costs[0] - profit_and_costs[1]
        if profit > 0:
            profit_all += profit
        firms[firm_name] = abs(profit)

with open('data_file.json', 'w', encoding='UTF-8') as write_file:
    json.dump([firms, {"average_profit": profit_all / len(firms)}], write_file)
print(firms)
print(profit_all)