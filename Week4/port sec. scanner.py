devices = [
    ("192.168.1.10", [80, 22, 74]),
    ("192.168.1.11", [143, 22, 25]),
    ("192.168.1.12", [80, 22, 443]),
    ("192.168.1.13", [993, 53, 71]),
    ("192.168.1.14", [80, 22, 23]),
    ("192.168.1.15", [49, 25, 53]),
    ("192.168.1.16", [80, 3389, 443]),
    ("192.168.1.17", [23, 22, 443]),
    ("192.168.1.18", [25, 21, 49]),
    ("192.168.1.19", [21, 22, 3389]),
]

risky_ports = [21, 993, 3389, 143]

def port_scan(device_list, ports_risks):
    print("Scanning ports...\n")
    i = 0
    for name, ports in device_list:
        for current_port in ports:
            if current_port not in ports_risks:
                continue
            else:
                print(f"{name} has risky port {current_port}")
                i = i + 1
    print(f"\nScanning done. {i} risky ports.")
port_scan(devices, risky_ports)