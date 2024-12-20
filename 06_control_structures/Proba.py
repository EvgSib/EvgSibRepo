def bin_ip(ip):
    octets = [int(o) for o in ip.split(".")]
    return ("{:08b}"*4).format(*octets)

print(bin_ip('10.255.17.0'))
