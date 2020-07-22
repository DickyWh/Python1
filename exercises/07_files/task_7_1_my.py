# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

with open('ospf.txt', 'r') as text:
    ospf = text.readlines()
    for lines in ospf:
        lines = lines.strip().split()
        protocol = lines[0].replace('O', 'OSPF')
        prefix = lines[1]
        ad = lines[2].strip('[]')
        hop = lines[4].strip(',')
        upd = lines[5].strip(',')
        intf = lines[6]
        ospf_row = '''
        Protocol:           {0}
        Prefix:             {1}
        AD/Metric:          {2}
        Next-Hop:           {3}
        Last update:        {4}
        Outbound Interface: {5}
        '''
        print(ospf_row.format(protocol,prefix,ad,hop,upd,intf))

