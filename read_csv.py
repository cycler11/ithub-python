from FW_rule import FWRule
import csv

def read_csv(file_path):
    rules = []
    with open(file_path, mode='r', encoding='cp1251') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            rule = FWRule(*row)
            rules.append(rule)
    return rules
