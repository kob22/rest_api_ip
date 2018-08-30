import unittest
from ip_validator import validate_address_ip

class IpValidatorTestCase(unittest.unittest.TestCase):
    """Tests for ip_validator.py"""

    def test_correct_ip(self):
        """Correct ip"""
        ip_list  = ['211.125.65.7', '78.58.21.152', '179.201.92.102', '169.159.176.196', '196.236.110.1']
        for ip in ip_list:
            validate_ip = validate_address_ip(ip)
            self.assertTrue(validate_ip)

    def test_only_digits_ip(self):
        """Incorrect ip - only digits"""
        ip_list = ['-179.220.244.214', '211.42.144.95-', 'a139.215.12.175', '25.184.2$30.57', '178.98.a.27']
        for ip in ip_list:
            validate_ip = validate_address_ip(ip)
            self.assertFalse(validate_ip)

    def test_range_ip(self):
        """test ip range 0-255"""
        ip_list = ['256.109.187.55', '110.400.67.105', '91.166.1000.140', '177.192.29.1090', '2000.225.4900.105']
        for ip in ip_list:
            validate_ip = validate_address_ip(ip)
            self.assertFalse(validate_ip)

    def test_ip4_format(self):
        """test ipv4 format(four digits and four dots)"""
        ip_list = ['38.73.21', '33.185.224,', '170,241.158.68', '135.199;145.109', '171.217.221-156']
        for ip in ip_list:
            validate_ip = validate_address_ip(ip)
            self.assertFalse(validate_ip)