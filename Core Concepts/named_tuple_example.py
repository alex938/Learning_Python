from collections import namedtuple

ipv4 = namedtuple("ipv4_data", ["ip_addr", "port"])
listener = ipv4("127.0.0.1", 1066)

print(type(listener.ip_addr))
print(listener.ip_addr)
print(listener.port)

print(listener[0])
print(listener[1])

for field in listener._fields:
    print(f"{field}: {getattr(listener, field)}")