import unittest

from handlers.tcp_handler import parse_package


class TCPHandlerTests(unittest.TestCase):

    def test_parse_package_should_return_right_value_field_package(self):
        dump = b'\x01\xbb\x38\xb3\xa4\x3b\x12\x4a\x25\xc4\x1b\x98\x50' \
               b'\x11\x00\x1f\xf3\xa2\x00\x00\x00\x00\x00\x00\x00\x00'

        expected_source_port = 443
        expected_destination_port = 14515
        expected_data_offset = 20
        expected_ns = 0
        expected_cwr = 0
        expected_ece = 0
        expected_urg = 0
        expected_ack = 1
        expected_psh = 0
        expected_rst = 0
        expected_syn = 0
        expected_fin = 1
        expected_window_size = 31
        expected_check_sum = 0xf3a2
        expected_urgent_pointer = 0

        package_value = parse_package(dump)

        self.assertEquals(expected_source_port, package_value[0])
        self.assertEquals(expected_destination_port, package_value[1])
        self.assertEquals(expected_data_offset, package_value[4])
        self.assertEquals(expected_ns, package_value[5])
        self.assertEquals(expected_cwr, package_value[6])
        self.assertEquals(expected_ece, package_value[7])
        self.assertEquals(expected_urg, package_value[8])
        self.assertEquals(expected_ack, package_value[9])
        self.assertEquals(expected_psh, package_value[10])
        self.assertEquals(expected_rst, package_value[11])
        self.assertEquals(expected_syn, package_value[12])
        self.assertEquals(expected_fin, package_value[13])
        self.assertEquals(expected_window_size, package_value[14])
        self.assertEquals(expected_check_sum, package_value[15])
        self.assertEquals(expected_urgent_pointer, package_value[16])
