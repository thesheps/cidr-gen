import unittest
from src.cidr_parser import to_ip_range


class TestCidrParser(unittest.TestCase):
    def test_cidr_block_returns_correct_number_of_ips(self):
        test_cases = [
            ("10.0.0.0/8", 16777216),
            ("10.0.0.0/24", 256),
            ("10.0.0.0/18", 16384),
            ("10.0.0.0/9", 8388608),
            ("10.0.0.0/30", 4),
        ]

        for value, expected in test_cases:
            with self.subTest(value=value):
                ips = to_ip_range(value)
                self.assertEqual(len(ips), expected)
