import unittest

from handlers.udp_handler import parse_package


class UDPHandlerTests(unittest.TestCase):

    def test_parse_package_should_return_right_value_field_package(self):
        dump = b'\x00\x44\x00\x43\x01\x43\x90\xfe\x01\x01\x06\x00\x5b\x8f\x6a\xae\x00\x00\x00\x00\x00' \
               b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x1a\x06\x92\xa8\xeb' \
               b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
               b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
               b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

        expected_source_port = 68
        expected_destination_port = 67
        expected_length = 323
        expected_checksum = 0x90fe

        package_value = parse_package(dump)

        self.assertEquals(expected_source_port, package_value[0])
        self.assertEquals(expected_destination_port, package_value[1])
        self.assertEquals(expected_length, package_value[2])
        self.assertEquals(expected_checksum, package_value[3])
