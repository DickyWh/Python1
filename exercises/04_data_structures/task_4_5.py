# -*- coding: utf-8 -*-
'''
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'


In [24]: command1 = 'switchport trunk allowed vlan 1,2,3,5,8'                   

In [25]: command2 = 'switchport trunk allowed vlan 1,3,8,9'                     

In [26]: com1 = command1.split()                                                

In [27]: print(com1)                                                            
['switchport', 'trunk', 'allowed', 'vlan', '1,2,3,5,8']

In [28]: vlans1 = com1[-1].split(',')                                           

In [30]: print(vlans1)                                                          
['1', '2', '3', '5', '8']

In [31]: com2 = command2.split()                                                

In [32]: print(com2)                                                            
['switchport', 'trunk', 'allowed', 'vlan', '1,3,8,9']

In [33]: vlans2 = com2[-1].split(',')                                           

In [34]: print(vlans2)                                                          
['1', '3', '8', '9']

In [35]: vlans = vlans1 + vlans2                                                

In [36]: print(vlans)                                                           
['1', '2', '3', '5', '8', '1', '3', '8', '9']

In [38]: vlans.sort()                                                           

In [39]: print(vlans)                                                           
['1', '1', '2', '3', '3', '5', '8', '8', '9']

In [43]: vlans.pop(1)                                                           
Out[43]: '1'

In [44]: print(vlans)                                                           
['1', '2', '3', '3', '5', '8', '8', '9']

In [45]: vlans.pop(2)                                                           
Out[45]: '3'

In [46]: vlans.pop(4)                                                           
Out[46]: '8'

In [47]: print(vlans)                                                           
['1', '2', '3', '5', '8', '9']

In [48]: vlans                                                                  
Out[48]: ['1', '2', '3', '5', '8', '9']





