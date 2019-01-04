import unittest
from src.cidr_parser import to_ip_range


class TestCidrParser(unittest.TestCase):
    def test_cidr_block_converts_to_ip_range(self):
        ips = to_ip_range("10.0.0.0/8")
        self.assertEqual(len(ips), 16777216)
