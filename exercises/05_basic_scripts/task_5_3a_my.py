# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

switchport = input ('Enter interface mode (access/trunk): ')
interface = input ('Enter interface type and number in format Fa0/7: ')




access_port = [
    'switchport mode access',
    'switchport access vlan {}',
    'switchport nonegotiate',
    'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]


trunk_port = [
    'switchport trunk encapsulation dot1q',
    'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

ports = {'access': access_port, 'trunk': trunk_port}
modes = {'access': 'Enter VLAN:', 'trunk': 'Enter allowed VLANs:' }

vlans = input (f'{modes[switchport]} ')


print('\n' + '-' * 30)

print('interface {}'.format(interface))

print('\n'.join(ports[switchport]).format(vlans))



