#!/usr/bin/env python3
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

output = "\n{:25} {}" * 6

res1 = ospf_route.replace(",", "").replace('[', '').replace(']', '').replace('O', 'OSPF').replace('via', '')

res = res1.split()



print(output.format(
"Protocol:",             res[0],
"Prefix:",               res[1],
"AD/Metric:",            res[2],
"Next-Hop:",             res[3],
"Last update:",          res[4],
"Outbound Interface:",   res[5],
))
