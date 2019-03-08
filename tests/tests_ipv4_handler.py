import unittest

from handlers.ipv4_handler import parse_package


class IPv4HandlerTests(unittest.TestCase):
    def test_parse_package_should_return_right_value_field_package(self):
        dump = b'\x45\x40\x00\x3c\x15\xa1\x00\x00\x36\x01\xa3\xca\x57\xf0\xa5\x57\xc0\xa8' \
               b'\x0d\x26\x00\x00\x54\xfe\x00\x01\x00\x5d\x61\x62\x63\x64\x65\x66' \
               b'\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76' \
               b'\x77\x61\x62\x63\x64\x65\x66\x67\x68\x69'

        expected_version_num = 4
        expected_header_len = 20
        expected_total_len = 60
        expected_package_identify = 5537
        expected_flag1 = 0
        expected_DF = 0
        expected_MF = 0
        expected_fragment_offset = 0
        expected_ttl = 54
        expected_next_protocol = 1
        expected_check_sum = 41930
        expected_sourse_ip = '87.240.165.87'
        expected_destination_ip = '192.168.13.38'

        package_value = parse_package(dump)

        self.assertEquals(expected_version_num, package_value[0])
        self.assertEquals(expected_header_len, package_value[1])
        self.assertEquals(expected_total_len, package_value[2])
        self.assertEquals(expected_package_identify, package_value[3])
        self.assertEquals(expected_flag1, package_value[4])
        self.assertEquals(expected_DF, package_value[5])
        self.assertEquals(expected_MF, package_value[6])
        self.assertEquals(expected_fragment_offset, package_value[7])
        self.assertEquals(expected_ttl,package_value[8])
        self.assertEquals(expected_next_protocol, package_value[9][0])
        self.assertEquals(expected_check_sum, package_value[10])
        self.assertEquals(expected_sourse_ip, package_value[11])
        self.assertEquals(expected_destination_ip, package_value[12])
