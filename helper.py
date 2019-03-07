def get_next_protocol(b, current_protocol):
    protocol = "unknown"

    if current_protocol == "ethernet":
        return get_next_protocol_for_ethernet(protocol, b)
    if current_protocol == "ipv4":
        return get_next_protocol_for_ipv4(protocol, b)


def get_next_protocol_for_ethernet(protocol, code):
    code = int.from_bytes(code, byteorder='big')

    if code == 0x0800:
        protocol = "IPv4"
        code = "08 00"
    elif code == 0x86DD:
        protocol = "IPv6"
        code = "86 DD"
    else:
        code = hex(code)[2:].zfill(4)

    return code, protocol


def get_next_protocol_for_ipv4(protocol, code):
    if code == 6:
        protocol = "TCP"
    if code == 17:
        protocol = "UDP"
    return code, protocol
