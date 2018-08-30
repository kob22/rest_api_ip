import unittest
from ip_validator import validate_address_ip
from ipaddress import ip_address, IPv4Address
class IpValidatorTestCase(unittest.TestCase):
    """Tests for ip_validator.py"""

    def test_correct_ip(self):
        """Correct ip"""
        ip_list  = ['211.125.65.7', '78.58.21.152', '179.201.92.102', '169.159.176.196', '196.236.110.1', '0.0.0.0', '255.255.255.255']
        for ip in ip_list:
            validate_ip = validate_address_ip(ip)
            validate_ip_ask = ip_address(ip)

            self.assertIsInstance(validate_ip_ask,
                                  IPv4Address)
            self.assertEqual(validate_ip, str(ip_address(ip)))
            self.assertEqual(validate_ip, ip)


    def test_correct_ip_with_digits(self):
        """Correct ip with digits"""
        ip_list  = ['008.2.5.6', '8.8.008.8', '001.002.004.000']
        correct_ip_list = ['8.2.5.6', '8.8.8.8', '1.2.4.0']
        for ip, correct_ip in zip(ip_list, correct_ip_list):
            validate_ip = validate_address_ip(ip)

            self.assertEqual(validate_ip, correct_ip)

    def test_only_digits_ip(self):
        """Incorrect ip - only digits"""
        ip_list = ['-179.220.244.214', '211.42.144.95-', 'a139.215.12.175', '25.184.2$30.57', '178.98.a.27']
        for ip in ip_list:
            validate_ip = validate_address_ip(ip)

            self.assertRaises(ValueError, ip_address, ip)
            self.assertFalse(validate_ip)

    def test_range_ip(self):
        """test ip range 0-255"""
        ip_list = ['256.109.187.55', '110.400.67.105', '91.166.1000.140', '177.192.29.1090', '2000.225.4900.105']
        for ip in ip_list:
            validate_ip = validate_address_ip(ip)
            self.assertRaises(ValueError, ip_address, ip)
            self.assertFalse(validate_ip)

    def test_ip4_format(self):
        """test ipv4 format(four digits and four dots)"""
        ip_list = ['38.73.21', '33.185.224,', '170,241.158.68', '135.199;145.109', '171.217.221-156', '....', '...3.3', '....23']
        for ip in ip_list:
            validate_ip = validate_address_ip(ip)
            self.assertRaises(ValueError, ip_address, ip)
            self.assertFalse(validate_ip)

    def test_ip6_format(self):
        """do not accept ipv6"""
        ip_list = ['2001:0db8:85a3:0000:0000:8a2e:0370:7334']
        for ip in ip_list:
            validate_ip = validate_address_ip(ip)

            self.assertFalse(validate_ip)

unittest.main()