import random
### DICTORINARIES
DNS_Servers = {
    'Cloudflare Primary': '1.1.1.1',
    'Cloudflare Secondary': '1.0.0.1',
    'Google Primary': '8.8.8.8',
    'Google Secondary': '8.8.4.4',
    'OpenDNS Primary': '208.67.222.222',
    'OpenDNS Secondary': '208.67.220.220',
}

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

### FUNCUTIONS
def Generate_Mac():
    mac_Adress = ':'.join(f'{random.randint(0, 255):02X}' for _ in range(6))
    return mac_Adress

def Random_Ip(): ### Generates New IP address using the 192.168.1 formatting scheme that's normal for most routers.
    starting_Octets = [192, 168, 1,]
    final_Octet = random.randint(1, 255)
    octets = starting_Octets + [final_Octet]
    ip_address = '.'.join(map(str, octets))
    return ip_address

### FUNCUTIONS


print("################# IP ADDRESS! AND MAC ####################")
print(f"{YELLOW}New IP Address: {Random_Ip()}{RESET}")
print(f"{YELLOW}New MAC Address: {Generate_Mac()}{RESET}")
print("################# IP ADDRESS! AND MAC ####################")
print("                                                           ")
print("DNS Servers if you need them! I would recommend cloudflare or openDNS")
for Provider, Address in DNS_Servers.items():
    print(f'{Provider}: {Address}')