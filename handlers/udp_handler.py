def handle_udp(package):
    package_value = parse_package(package)
    print_parsed_package(package_value[:-1])

    return package_value


def parse_package(package):
    source_port = int.from_bytes(package[0:2], byteorder='big')
    destination_port = int.from_bytes(package[2:4], byteorder='big')

    package_length = int.from_bytes(package[4:6], byteorder='big')
    check_sum = int.from_bytes(package[6:8], byteorder='big')
    data = package[8:]

    return [source_port, destination_port, package_length, check_sum, data]


def print_parsed_package(args):
    source_port, destination_port, package_length, check_sum = args
    print('Sourse port:', source_port)
    print('Destination port:', destination_port)

    print('Package_length:', package_length)
    print('Check summ:', check_sum)
