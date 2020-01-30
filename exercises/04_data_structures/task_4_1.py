# -*- coding: utf-8 -*-
'''
Задание 4.1

Обработать строку nat таким образом,
чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet.

Ограничение: Все задания надо выполнять используя только пройденные темы.


'''

nat = 'ip nat inside source list ACL interface FastEthernet0/1 overload'

In [9]: nat.replace('Fast', 'Gigabit')                                          
Out[9]: 'ip nat inside source list ACL interface GigabitEthernet0/1 overload'

In [10]: nat = nat.replace('Fast', 'Gigabit')                                   

In [11]: nat                                                                    
Out[11]: 'ip nat inside source list ACL interface GigabitEthernet0/1 overload'

In [12]: print(nat)                                                             
ip nat inside source list ACL interface GigabitEthernet0/1 overload
