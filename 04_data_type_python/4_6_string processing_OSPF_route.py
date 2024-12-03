"""
Обработать строку ospf_route и вывести информацию на стандартный поток
вывода в виде:
Prefix              10.0.24.0/24
AD/Metric           110/41
Next-Hop            10.0.13.3
Last update         3d18h
Outbound Interface  FastEthernet0/0
"""

ospf_route = " 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ip_template = '''
Prefix              {}
AD/Metric           {:<16}
Next-Hop            {:<16}
Last update         {:<16}
Outbound Interface  {:<16}
'''

ospf_route = ospf_route.replace('[', '')
ospf_route = ospf_route.replace(']', '')
ospf_route = ospf_route.replace(',', '')
ospf_route = ospf_route.split()
print(ip_template.format(ospf_route[0], ospf_route[1], ospf_route[3], ospf_route[4], ospf_route[5]))
