import unittest

from handlers.ethernet_handler import parse_package


class EthernetHandlerTests(unittest.TestCase):
    def test_parse_package_should_return_right_value_field_package(self):
        damp = b'\x20\x1a\x06\x92\xa8\xeb\x0e\x5d\x4e\x97\xf6\xa0\x08\x00\x45\x40' \
               b'\x00\x3c\x15\xa1\x00\x00\x36\x01\xa3\xca\x57\xf0\xa5\x57\xc0\xa8' \
               b'\x0d\x26\x00\x00\x54\xfe\x00\x01\x00\x5d\x61\x62\x63\x64\x65\x66' \
               b'\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76' \
               b'\x77\x61\x62\x63\x64\x65\x66\x67\x68\x69'

        expected_destination_mac = '20:1a:06:92:a8:eb'
        expected_source_mac = '0e:5d:4e:97:f6:a0'
        expected_next_protocol = "IPv4"

        package_value = parse_package(damp)
        actual_destination = package_value[0]
        actual_source = package_value[1]
        actual_next_protocol = package_value[2][1]

        self.assertEquals(expected_destination_mac, actual_destination)
        self.assertEquals(expected_source_mac, actual_source)
        self.assertEquals(expected_next_protocol, actual_next_protocol)
