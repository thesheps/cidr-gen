from src.netmask_converter import cidr_to_binary


def to_ip_range(cidr):
    binary = cidr_to_binary(cidr)
    flipped = ""

    for c in binary:
        if c == "1":
            flipped += "0"
        if c == "0":
            flipped += "1"

    return int(flipped, 2) + 1
