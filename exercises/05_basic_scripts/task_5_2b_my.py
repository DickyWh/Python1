#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv

network = argv[1]

net = network.split('/')
ip = net[0]
mask = net[1]
ip = ip.split('.')
ip_o1 = int(ip[0])
ip_o2 = int(ip[1])
ip_o3 = int(ip[2])
ip_o4 = 0 * (int(ip[3]))

maskint = int(mask)
maskbit = '1' * maskint
maskbit = "{:<032}".format(maskbit)
mask_o1 = int(maskbit[0:8], 2)
mask_o2 = int(maskbit[8:16], 2)
mask_o3 = int(maskbit[16:24], 2)
mask_o4 = int(maskbit[24:32], 2)

template = '''
    : Network:
    : {0:<8} {1:<8} {2:<8} {3:<8}
    : {0:<08b} {1:<08b} {2:<08b} {3:<08b}

    : Mask:
    : /{8:<}
    : {4:<8} {5:<8} {6:<8} {7:<8}
    : {4:<08b} {5:<08b} {6:<08b} {7:<08b}
'''
print(template.format(ip_o1, ip_o2, ip_o3, ip_o4, mask_o1, mask_o2, mask_o3, mask_o4, mask))



