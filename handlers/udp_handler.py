def handle_udp(package):
    source_port = package[0:2]
    destination_port = package[2:4]

    package_length = package[4:6]
    check_sum = package[6:8]
    data = package[8:]
    package_value = source_port, destination_port, package_length, check_sum
    print_parsed_package(package_value)

    return package_value


def print_parsed_package(args):
    source_port, destination_port, package_length, check_sum = args
    print('Sourse port:', source_port)
    print('Destination port:', destination_port)

    print('Package_length:', package_length)
    print('Check summ:', check_sum)
