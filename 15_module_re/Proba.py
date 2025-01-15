import re
from pprint import pprint

line1 = 'interface Ethernet0/1'
line2 = ' ip address 10.255.2.2 255.255.255.0'
line3 = ' ip address 10.254.2.2 255.255.255.0 secondary'


regex = (r"^interface (?P<intf>\S+)"
             r"|address (?P<ip>\S+) (?P<mask>\S+)")

match = re.search(regex, line)


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




