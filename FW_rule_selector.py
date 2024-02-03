from datetime import datetime, timedelta

class FWRuleSelector:
    def __init__(self, rules):
        self.rules = rules

    def get_network_addresses(self):
        addresses = set()
        for rule in self.rules:
            addresses.add(rule.source_ip)
            addresses.add(rule.destination_ip)
        return list(addresses)

    def get_allow_rules(self, network_address):
        allow_rules = []
        for rule in self.rules:
            if rule.action == 'permit' and (rule.source_ip == network_address or rule.destination_ip == network_address):
                allow_rules.append(rule)
        return allow_rules

    def get_deny_rules(self, network_address):
        deny_rules = []
        for rule in self.rules:
            if rule.action == 'forbid' and (rule.source_ip == network_address or rule.destination_ip == network_address):
                deny_rules.append(rule)
        return deny_rules

    def get_standard_ports_access_rules(self):
        standard_ports_rules = []
        for rule in self.rules:
            if '22' in rule.ports or '3389' in rule.ports or '80' in rule.ports or '443' in rule.ports:
                standard_ports_rules.append(rule)
        return standard_ports_rules

    def get_file_server_access_rules(self):
        file_server_rules = []
        for rule in self.rules:
            if '21' in rule.ports:
                file_server_rules.append(rule)
        return file_server_rules

    def get_old_rules(self):
        old_rules = []
        for rule in self.rules:
            try:
                rule_date = datetime.strptime(rule.timestamp, '%Y-%m-%d %H:%M:%S.%f+00:00')
                if datetime.now() - rule_date > timedelta(days=365):
                    old_rules.append(rule)
            except ValueError as e:
                print(f"Ignoring rule with invalid timestamp: {rule.timestamp}")
        return old_rules

    def get_recent_rules(self):
        recent_rules = []
        for rule in self.rules:
            try:
                rule_date = datetime.strptime(rule.timestamp, '%Y-%m-%d %H:%M:%S.%f+00:00')
                if datetime.now() - rule_date <= timedelta(days=90):
                    recent_rules.append(rule)
            except ValueError as e:
                print(f"Ignoring rule with invalid timestamp: {rule.timestamp}")
        return recent_rules
