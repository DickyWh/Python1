# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface     FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

In [1]: ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'  

In [9]: template = ''' 
   ...: Protocol:           {} 
   ...: Prefix:             {} 
   ...: AD/Metric:          {} 
   ...: Next-Hop:           {} 
   ...: Last update:        {} 
   ...: Outbound Interface: {} 
   ...: '''                                                                     

In [10]: template.format('OSPF', '10.0.24.0/24', '110/41', '10.0.13.3', '3d18h',
    ...:  'FastEthernet0/0')                                                    
Out[10]: '\nProtocol: OSPF\nPrefix: 10.0.24.0/24\nAD/Metric: 110/41\nNext-Hop: 10.0.13.3\nLast update: 3d18h\nOutbound Interface: FastEthernet0/0\n'

print(template)                                                        

Protocol:           {}
Prefix:             {}
AD/Metric:          {}
Next-Hop:           {}
Last update:        {}
Outbound Interface: {}

In [18]: print(template.format('OSPF', '10.0.24.0/24', '110/41', '10.0.13.3', '3
    ...: d18h', 'FastEthernet0/0'))                                             

Protocol:           OSPF
Prefix:             10.0.24.0/24
AD/Metric:          110/41
Next-Hop:           10.0.13.3
Last update:        3d18h
Outbound Interface: FastEthernet0/0


In [19]: ospf_route_row = template.format('OSPF', '10.0.24.0/24', '110/41', '10.
    ...: 0.13.3', '3d18h', 'FastEthernet0/0')                                   

In [20]: print(ospf_route_row)                                                  

Protocol:           OSPF
Prefix:             10.0.24.0/24
AD/Metric:          110/41
Next-Hop:           10.0.13.3
Last update:        3d18h
Outbound Interface: FastEthernet0/0

In [21]: template = ''' 
    ...: Protocol:           {pr} 
    ...: Prefix:             {pref} 
    ...: AD/Metric:          {metric} 
    ...: Next-Hop:           {NextHop} 
    ...: Last update:        {LastUp} 
    ...: Outbound Interface: {Intf} 
    ...: '''                                                                                              

In [22]: ospf_route_row = template.format(pr='OSPF', pref='10.0.24.0/24', metric='110/41', NextHop='10.0.1
    ...: 3.3', LastUp='3d18h', Intf='FastEthernet0/0')                                                    

In [23]: print(ospf_route_row)                                                                            

Protocol:           OSPF
Prefix:             10.0.24.0/24
AD/Metric:          110/41
Next-Hop:           10.0.13.3
Last update:        3d18h
Outbound Interface: FastEthernet0/0

