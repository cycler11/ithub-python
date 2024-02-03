import csv

def save_to_csv(rules, file_path):
    with open(file_path, mode='w', encoding='cp1251', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for rule in rules:
            writer.writerow([
                rule.timestamp,
                rule.source_ip,
                rule.source_subnet,
                rule.destination_ip,
                rule.destination_subnet,
                rule.ports,
                rule.action
            ])
