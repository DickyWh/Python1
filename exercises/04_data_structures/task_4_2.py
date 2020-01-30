# -*- coding: utf-8 -*-
'''
Задание 4.2

Преобразовать строку mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

mac = 'AAAA:BBBB:CCCC'

In [13]: mac = 'AAAA:BBBB:CCCC'                                                 

In [14]: mac.replace(':', '.')                                                  
Out[14]: 'AAAA.BBBB.CCCC'

In [15]: mac = mac.replace(':', '.')                                            

In [16]: print(mac)                                                             
AAAA.BBBB.CCCC
