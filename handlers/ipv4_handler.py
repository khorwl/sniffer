from helper import get_next_protocol
from handlers.tcp_handler import handle_tcp
from handlers.udp_handler import handle_udp


def handle_ipv4(package):
    package_values = parse_package(package)

    print_parsed_package(package_values[:-1])

    next_protocol = package_values[9]
    data = package_values[-1]

    if next_protocol[0] == 6:
        handle_tcp(data)
    if next_protocol[0] == 17:
        handle_udp(data)

    return package_values


def parse_package(package):
    version_num = package[0] >> 4
    header_len = (package[0] & 0x0f) * 4
    service_type = package[1]
    total_len = int.from_bytes(package[2:4], byteorder='big')

    package_identify = int.from_bytes(package[4:6], byteorder='big')
    flag1 = package[6] >> 7
    DF = (package[6] >> 6) & 0x01
    MF = (package[6] >> 5) & 0x01
    fragment_offset = ((package[6] & 0x1f) << 8) * 256 + package[7]

    ttl = package[8]
    next_protocol = get_next_protocol(package[9], "ipv4")
    check_sum = int.from_bytes(package[10:12], byteorder='big')

    source_ip = get_ipv4(package[12:16])
    destination_ip = get_ipv4(package[16:20])
    data = package[header_len:]

    return [version_num, header_len, total_len, package_identify, flag1, DF, MF,
            fragment_offset, ttl, next_protocol, check_sum, source_ip, destination_ip, data]


def print_parsed_package(args):
    version_num, header_len, total_len, package_identify, flag1, DF, MF, \
    fragment_offset, ttl, next_protocol, check_sum, source_ip, \
    destination_ip = args

    print('\n\rVersion number:', version_num)
    print('Header lenght:', header_len)
    print('Total lenght:', total_len)

    print('Package identify:', package_identify)
    print('First flag:', flag1)
    print('DF flag:', DF)
    print('MF flag:', MF)
    print('Fragment offset:', fragment_offset)

    print('Time to live:', ttl)
    print('Next protocol:', next_protocol)
    print('Check summ:', check_sum)

    print('Sourse IP:', source_ip)
    print('Destination IP:', destination_ip)


def get_ipv4(b):
    return '.'.join(map(lambda x: str(x), b))
