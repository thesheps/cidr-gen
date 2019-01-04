import unittest
from src.netmask_converter import cidr_to_netmask, netmask_to_cidr_prefix


class TestNetmaskConverter(unittest.TestCase):
    def test_netmask_returns_correct_cidr_prefix(self):
        test_cases = [
            ("128.0.0.0", 1),
            ("192.0.0.0", 2),
            ("224.0.0.0", 3),
            ("240.0.0.0", 4),
            ("248.0.0.0", 5),
            ("252.0.0.0", 6),
            ("254.0.0.0", 7),
            ("255.0.0.0", 8),
            ("255.128.0.0", 9),
            ("255.255.0.0", 16),
            ("255.255.255.0", 24),
            ("255.255.255.255", 32)
        ]

        for value, expected in test_cases:
            with self.subTest(value=value):
                prefix = netmask_to_cidr_prefix(value)
                self.assertEqual(prefix, expected)

    def test_cidr_block_returns_correct_netmask(self):
        test_cases = [
            ("10.0.0.0/1", "128.0.0.0"),
            ("10.0.0.0/2", "192.0.0.0"),
            ("10.0.0.0/3", "224.0.0.0"),
            ("10.0.0.0/4", "240.0.0.0"),
            ("10.0.0.0/5", "248.0.0.0"),
            ("10.0.0.0/6", "252.0.0.0"),
            ("10.0.0.0/7", "254.0.0.0"),
            ("10.0.0.0/8", "255.0.0.0"),
            ("10.0.0.0/9", "255.128.0.0"),
            ("10.0.0.0/16", "255.255.0.0"),
            ("10.0.0.0/24", "255.255.255.0"),
            ("10.0.0.0/32", "255.255.255.255")
        ]

        for value, expected in test_cases:
            with self.subTest(value=value):
                netmask = cidr_to_netmask(value)
                self.assertEqual(netmask, expected)
