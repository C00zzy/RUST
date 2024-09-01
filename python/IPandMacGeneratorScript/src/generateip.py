import random
DNS_Servers = {
    'Cloudflare Primary': '1.1.1.1',
    'Cloudflare Secondary': '1.0.0.1',
    'Google Primary': '8.8.8.8',
    'Google Secondary': '8.8.4.4',
    'OpenDNS Primary': '208.67.222.222',
    'OpenDNS Secondary': '208.67.220.220',
}

### FUNCTIONS
def Grab_DNS():
    """Prints the list of DNS servers."""
    for server, address in DNS_Servers.items():
        print(f'{server}: {address}')

def Generate_IP():
    """Generates a new IP address using the 192.168.1.x format."""
    starting_octets = [192, 168, 1]
    final_octet = random.randint(1, 255)
    octets = starting_octets + [final_octet]
    ip_address = '.'.join(map(str, octets))
    return ip_address

def Generate_MAC():
    """Generates a random MAC address."""
    mac_address = ':'.join(f'{random.randint(0, 255):02X}' for _ in range(6))
    return mac_address

def Main_Menu():
    """Returns the menu prompt string."""
    return (
        "Welcome!\n"
        "Press 1 for a random IP Address\n"
        "Press 2 for a random MAC Address\n"
        "Press 3 for a list of DNS servers\n"
        "Type 'exit' to exit.\n"
        "Choose an option: "
    )
### FUNCTIONS

while True:
    option = input(Main_Menu())
    if option == '1':
        print(Generate_IP())
        break
    elif option == '2':
        print(Generate_MAC())
        break
    elif option == '3':
        Grab_DNS()
        break
    elif option.lower() == 'exit':
        print("Exiting")
        break
    else:
        print("Invalid option, please try again.")

# Comments added by AI; overall structure done by me.
# I'm not a genius programmer, so implementation ideas were developed using Google and AI.
# To be honest, using Google and AI is essentially the same, and most people will use AI to figure shit out.
# It reminds me of when I was learning Linux; I always used Google.
# The same principle applies here.
# I should use multiline comments here, but I won't because fuck you.
# And people who dog on other programmers for using google, AI, Dude i just want to code for fun
# and not bash my fucking head against my desk trying to figure shit out man thats not fun
# For production i mean those programmers are college trained or been coding since they were a sperm cell 
# Plus if you know what the code does, Is it really bad? to me its only bad if you don't know what the code actually does
# And i've been programming on and off for only like a year.