import unittest
from app_core import get_northcountires_names


class countryNameTestCase(unittest.TestCase):

    def testSingleCountry(self):
        ip = ['8.8.8.8']
        country_name = get_northcountires_names(ip)

        self.assertSequenceEqual(country_name, ['United States'])

    def testsouthcountry(self):
        ip = ['179.64.0.0']
        country_name = get_northcountires_names(ip)

        self.assertSequenceEqual(country_name, [])

    def testnocountry(self):
        ip = []
        country_name = get_northcountires_names(ip)

        self.assertSequenceEqual(country_name, [])

    def testtoo_many(self):
        ips = ['8.8.8.8','138.8.8.8', '45.8.8.8', '10.8.8.8', '32.8.2.8', '22.8.77.8']

        country_name = get_northcountires_names(ips)
        self.assertSequenceEqual(country_name, [])

    def testnorthAndSouthCountry(self):
        ips = ['8.8.8.8', '179.64.0.0', '157.253.0.0', '2.92.0.0', '1.120.0.0']

        country_name = get_northcountires_names(ips)
        self.assertSequenceEqual(country_name, ['Colombia', 'Russia', 'United States'])

    def testwithletters(self):
        ips = ['88.8.8', '179.64.0.0', '157.253.0.0', '2.92.0.0', '1.f.0.0']

        country_name = get_northcountires_names(ips)
        self.assertSequenceEqual(country_name, ['Colombia', 'Russia'])


unittest.main()