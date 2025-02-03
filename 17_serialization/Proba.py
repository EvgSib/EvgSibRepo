import re
from pprint import pprint
import csv
import glob
import yaml


to_yaml = {
'access': ['switchport mode access',
'switchport access vlan',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable'],
'trunk': ['switchport trunk encapsulation dot1q',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan'],
}
with open('sw_templates.yaml', 'w') as f:
    yaml.dump(to_yaml, f)
with open('sw_templates.yaml') as f:
    print(f.read())

# line1 = 'SW1>show cdp neighbors'
# line2 = 'R1           Eth 0/1         122           R S I           2811       Eth 0/0'
# line3 = ' '

# match = re.search(regex, line3)
# if match:
#     print(match.group())
#     print(match.groups())
#     print(match.group('hostname', 'Device_ID', 'Local_Intrfce', 'Port_ID'))
#     print(match.lastgroup)

# result = {}
# dictList = [{'Eth 0/1': {'R1': 'Eth 0/0'}},{'Eth 0/2': {'R2': 'Eth 0/0'}}, {'Eth 0/3': {'R3': 'Eth 0/0'}}, {'Eth 0/4': {'R4': 'Eth 0/0'}}]
# hostname = 'SW2'

# newDict = {k:v for element in dictList for k,v in element.items()}
# result[hostname] = newDict
# pprint(result)


