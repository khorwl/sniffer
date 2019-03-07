from handlers.tcp_handler import handle_tcp
from handlers.udp_handler import handle_udp


def get_ipv6(b):
    return ':'.join(map(lambda x: hex(x)[2:], b))


def handle_ipv6(package):
    version_num = package[0] >> 4
    traffic_class = (package[0] & 0x0f) * 256 + (package[1] >> 4)
    stream_label = ((package[1] & 0x0f) << 16) + int.from_bytes(package[2:4], byteorder='big')

    payload_length = int.from_bytes(package[4:6], byteorder='big')
    next_header = package[6]
    number_transit_sections = package[7]

    source_ip = get_ipv6(package[8:24])
    destination_ip = get_ipv6(package[24:40])
    data = package[len(package) - payload_length:]

    package_values = [version_num, traffic_class, stream_label, payload_length, next_header,
                      number_transit_sections, source_ip, destination_ip]
    print_parsed_package(package_values)

    tcp_code = 6
    udp_code = 17

    if next_header == tcp_code:
        handle_tcp(data)
    if next_header == udp_code:
        handle_udp(data)

    return package_values


def print_parsed_package(args):
    version_num, traffic_class, stream_label, payload_length, next_header, \
    number_transit_sections, source_ip, destination_ip = args

    print('Version number:', version_num)
    print('Traffic class:', traffic_class)
    print('Stream label:', stream_label)

    print('Payload_length:', payload_length)
    print('Next header:', next_header)
    print('Number of transit sections:', number_transit_sections)

    print('Source IP:', source_ip)
    print('Destination IP:', destination_ip, '\n\r')
