import re
from pprint import pprint

with open("sh_version_r1.txt") as f:
    file_str = f.read()
    print(file_str)




# line1 = 'MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface'
# line2 = '00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20'
# line3 = 'Total number of bindings: 2'


# regex = (r'(?P<mac>\S+) +(?P<ip>\S+) +\d+ +\S+ +\d+ +(?P<intf>\S+)')

# match = re.search(regex, line2)
# print(match.group())
# print(match.groups())
# print(match.group('intf'))

# regex = (r'interface (?P<intf>\S+)'
#          r'|ip address (?P<ip>\S+) (?P<mask>\S+)')

# match = re.search(regex, line3)
# print(match.group())
# print(match.groups())
# print(match.group('intf'))



# result = {}
# with open(config) as f:
#     for line in f:
#         match = re.search(regex, line)
#         if match:
#             if match.lastgroup == 'intf':
#                 interface = match.group('intf')
#             else:
#                 result[interface] = match.group('ip', 'mask')




