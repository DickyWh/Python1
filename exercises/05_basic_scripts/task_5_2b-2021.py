# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

#network = input('Введите инфу о сети в формате x.x.x.x/24: ')

from sys import argv

network = argv[1]
network1 = network.split('/')

ip = network1[0]
mask = network1[1]
mask = int(mask)

ip = ip.split('.')
ip_o1 = int(ip[0])
ip_o2 = int(ip[1])
ip_o3 = int(ip[2])
ip_o4 = int(ip[3])

bin_ip_str = "{:08b}{:08b}{:08b}{:08b}".format(ip_o1, ip_o2, ip_o3, ip_o4)
bin_network_str = bin_ip_str[:mask] + '0' * (32 - mask)

net1 = int(bin_network_str[0:8], 2)
net2 = int(bin_network_str[8:16], 2)
net3 = int(bin_network_str[16:24], 2)
net4 = int(bin_network_str[24:32], 2)

maskbit = '1' * mask
maskbit = '{:<032}'.format(maskbit)

m1 = int(maskbit[0:8], 2)
m2 = int(maskbit[8:16], 2)
m3 = int(maskbit[16:24], 2)
m4 = int(maskbit[24:32], 2)

ip_out = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''

mask_out = '''
Mask:
/{0}
{1:<8} {2:<8} {3:<8} {4:<8}
{1:08b} {2:08b} {3:08b} {4:08b}
'''

print(ip_out.format(net1, net2, net3, net4))

print(mask_out.format(mask, m1, m2, m3, m4))
