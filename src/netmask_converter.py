def to_netmask(cidr):
    length = int(cidr.split("/")[-1])
    binary = length * "1" + (32 - length) * "0"
    octets = [binary[i:i+8] for i in range(0, len(binary), 8)]

    return ".".join(str(int(s, 2)) for s in octets)