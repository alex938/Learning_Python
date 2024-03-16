from colorama import init, Back, Fore
from collections import namedtuple
init(autoreset = True)

ipv4 = namedtuple("ipv4_data",["ip_addr", "port", "protocol"])
listener = ipv4("127.0.0.1", 1066, "tcp")

print(Back.GREEN + str(listener))
print(listener.ip_addr)
print(listener.port)

print(listener[0])
print(listener[1])
print(listener[2])

print(len(listener))