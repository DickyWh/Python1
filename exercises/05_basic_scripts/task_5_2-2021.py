# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

net = input('Введите инфу о сети в формате x.x.x.x/24: ')
net1 = net.split('/')

ip = net1[0]
mask = net1[1]

ip = ip.split('.')
ip_o1 = int(ip[0])
ip_o2 = int(ip[1])
ip_o3 = int(ip[2])
ip_o4 = int(ip[3])


maskint = int(mask)
maskbit = '1' * maskint
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
print(ip_out.format(ip_o1, ip_o2, ip_o3, ip_o4))
#print('-'*40)
print (mask_out.format(maskint, m1, m2, m3, m4))


