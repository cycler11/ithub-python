from FW_rule import FWRule
from FW_rule_selector import FWRuleSelector
from read_csv import read_csv
from save_to_csv import save_to_csv

# read from csv file with FW rules
rules = read_csv('fw_rules_v2.csv')

# selector object creation
selector = FWRuleSelector(rules)

# all network ip address
network_addresses = selector.get_network_addresses()
print("Network ip addresses:", network_addresses)

# all allow rules
for address in network_addresses:
    allow_rules = selector.get_allow_rules(address)
    print("Allow rules:", address, ":")
    for rule in allow_rules:
        print(rule.timestamp, rule.source_ip, rule.destination_ip, rule.ports, rule.action)

# all deny rules
for address in network_addresses:
    deny_rules = selector.get_deny_rules(address)
    print("Deny rules:", address, ":")
    for rule in deny_rules:
        print(rule.timestamp, rule.source_ip, rule.destination_ip, rule.ports, rule.action)

# SSH, rdp
standard_ports_access_rules = selector.get_standard_ports_access_rules()
print("RDP & SSH:")
for rule in standard_ports_access_rules:
    print(rule.timestamp, rule.source_ip, rule.destination_ip, rule.ports, rule.action)

# FTP
file_server_access_rules = selector.get_file_server_access_rules()
print("FTP Rules:")
for rule in file_server_access_rules:
    print(rule.timestamp, rule.source_ip, rule.destination_ip, rule.ports, rule.action)

# year ago rules
old_rules = selector.get_old_rules()
print("Old rules:")
for rule in old_rules:
    print(rule.timestamp, rule.source_ip, rule.destination_ip, rule.ports, rule.action)

# last 3 months
recent_rules = selector.get_recent_rules()
print("Recent rules:")
for rule in recent_rules:
    print(rule.timestamp, rule.source_ip, rule.destination_ip, rule.ports, rule.action)

# save to csv
save_to_csv(allow_rules, 'allow_rules.csv')
save_to_csv(deny_rules, 'deny_rules.csv')
save_to_csv(standard_ports_access_rules, 'standard_ports_access_rules.csv')
save_to_csv(file_server_access_rules, 'file_server_access_rules.csv')
save_to_csv(old_rules, 'old_rules.csv')
save_to_csv(recent_rules, 'recent_rules.csv')

# needs to be fixed