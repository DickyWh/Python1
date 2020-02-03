# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

mac = 'AAAA:BBBB:CCCC'

In [1]: mac = 'AAAA:BBBB:CCCC'                                                                            

In [2]: mac = mac.split(':')                                                                              

In [3]: mac                                                                                               
Out[3]: ['AAAA', 'BBBB', 'CCCC']

In [4]: print(mac)                                                                                        
['AAAA', 'BBBB', 'CCCC']

In [5]: len(mac)                                                                                          
Out[5]: 3

In [7]: '{:b}{:b}{:b}'.format(0xAAAA, 0xBBBB, 0xCCCC)                                                     
Out[7]: '101010101010101010111011101110111100110011001100'

In [8]: mac = '{:b}{:b}{:b}'.format(0xAAAA, 0xBBBB, 0xCCCC)                                               

In [9]: print(mac)                                                                                        
101010101010101010111011101110111100110011001100



