def to_netmask(cidr):
    length = int(cidr.split("/")[-1])
    binary = length * "1" + (32 - length) * "0"
    octets = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ".".join(str(int(s, 2)) for s in octets)


def to_cidr_prefix(netmask):
    octets = netmask.split(".")
    binary = "".join([format(int(i), "08b") for i in octets])
    return binary.count("1")
