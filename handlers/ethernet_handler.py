from helper import get_next_protocol
from handlers.ipv4_handler import handle_ipv4
from handlers.ipv6_handler import handle_ipv6


def handle_ethernet(package):
    package_value = parse_package(package)
    print_parsed_package(package_value[:-1])

    next_protocol = package_value[2]
    data = package_value[-1]

    if next_protocol[1] == "IPv4":
        handle_ipv4(data)
    if next_protocol[1] == "IPv6":
        handle_ipv6(data)

    return package_value


def parse_package(package):
    destination_mac = get_mac(package[0:6])
    source_mac = get_mac(package[6:12])
    next_protocol = get_next_protocol(package[12:14], "ethernet")
    data = package[14:]

    return [destination_mac, source_mac, next_protocol, data]


def print_parsed_package(args):
    destination_mac, source_mac, next_protocol = args

    print('\n\r****************************************')
    print('Destination MAC:', destination_mac)
    print('Source MAC:', source_mac)
    print('Next protocol:', next_protocol)


def get_mac(b):
    return ':'.join(map(lambda x: hex(x)[2:].zfill(2), b))
