# -*- coding: utf-8 -*-
'''
Задание 4.3

Получить из строки config список VLANов вида:
['1', '3', '10', '20', '30', '100']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

config = 'switchport trunk allowed vlan 1,3,10,20,30,100'


In [13]: config = 'switchport trunk allowed vlan 1,3,10,20,30,100'              

In [14]: commands = config.split()                                              

In [15]: print(commands)                                                        
['switchport', 'trunk', 'allowed', 'vlan', '1,3,10,20,30,100']

In [16]: vlans = commands[-1].split(',')                                        

In [17]: print(vlans)                                                           
['1', '3', '10', '20', '30', '100']
