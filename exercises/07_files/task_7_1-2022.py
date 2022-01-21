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
output = "\n{:25} {}" * 6

with open("ospf.txt", "r") as f:
    for line in f:
        rows = line.replace("O", "OSPF").replace(",", " ").replace("[", "").replace("]", "")
        rows = rows.split()
        
        print(output.format(
                "Protocol", rows[0],
                "Prefix", rows[1],
                "AD/Metric", rows[2],
                "Next-Hop", rows[4],
                "Last update", rows[5],
                "Outbound Interface", rows[6],
        ))
