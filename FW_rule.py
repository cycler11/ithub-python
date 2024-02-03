class FWRule:
    def __init__(self, timestamp, source_ip, source_subnet, destination_ip, destination_subnet, ports, action):
        self.timestamp = timestamp
        self.source_ip = source_ip
        self.source_subnet = source_subnet
        self.destination_ip = destination_ip
        self.destination_subnet = destination_subnet
        self.ports = ports
        self.action = action
