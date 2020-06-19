# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip = input('Введите IP-адрес в формате х.х.х.х: ').strip().split('.')
ip_o1 = int(ip[0])
ip_o2 = int(ip[1])
ip_o3 = int(ip[2])
ip_o4 = int(ip[3])

unicast = list(range(1, 224))
multicast = list(range(224, 240))
broadcast = [255,255,255,255]
unassigned = [0,0,0,0]

if ip_o1 in unicast:
    print('Это unicast IP-адрес')
elif ip_o1 in multicast:
    print('Это multicast IP-адрес')
elif ip_o1 in broadcast and ip_o2 in broadcast and ip_o3 in broadcast and ip_o4 in broadcast:
    print('Это broadcast IP-адрес')
elif ip_o1 in unassigned and ip_o2 in unassigned and ip_o3 in unassigned and ip_o4 in unassigned:
    print('Это неназначенный IP-адрес')
else:
    print('Это unused (неиспользуемый) IP-адрес')



