def handle_tcp(package):
    source_port = int.from_bytes(package[0:2], byteorder='big')
    destination_port = int.from_bytes(package[2:4], byteorder='big')

    sequence_number = int.from_bytes(package[4:8], byteorder='big')
    acknowledgment_number = int.from_bytes(package[8:12], byteorder='big')

    data_offset = package[12] >> 4

    ns = package[12] & 0x01
    cwr = package[13] >> 7
    ece = (package[13] >> 6) & 0x01
    urg = (package[13] >> 5) & 0x01
    ack = (package[13] >> 4) & 0x01
    psh = (package[13] >> 3) & 0x01
    rst = (package[13] >> 2) & 0x01
    syn = (package[13] >> 1) & 0x01
    fin = package[13] & 0x01

    window_size = int.from_bytes(package[14:16], byteorder='big')
    check_sum = int.from_bytes(package[16:18], byteorder='big')
    urgent_pointer = int.from_bytes(package[18:20], byteorder='big')

    package_value = [source_port, destination_port, sequence_number,
                     acknowledgment_number, data_offset, ns, cwr, ece, urg,
                     ack, psh, rst, syn, fin, window_size, check_sum, urgent_pointer]
    print_parsed_package(package_value)

    data = package[20:]

    return package_value


def print_parsed_package(args):
    source_port, destination_port, sequence_number, \
    acknowledgment_number, data_offset, ns, cwr, ece, urg,\
    ack, psh, rst, syn, fin, window_size, check_sum, urgent_pointer = args

    print('\n\rSourse port:', source_port)
    print('Destination port:', destination_port)

    print('Sequence number:', sequence_number)
    print('Acknowledgment number :', acknowledgment_number)
    print('Data offset:', data_offset)

    print("Flags:")
    print(' NS:', ns)
    print(' CWR:', cwr)
    print(' ECE:', ece)

    print(' URG:', urg)
    print(' ACK:', ack)
    print(' PSH:', psh)
    print(' RST:', rst)
    print(' SYN:', syn)
    print(' FIN:', fin)

    print('Window size:', window_size)
    print('Check summ:', check_sum)
    print('Urgent pointer:', urgent_pointer)
