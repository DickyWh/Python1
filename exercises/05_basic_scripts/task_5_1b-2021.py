# -*- coding: utf-8 -*-
'''
Задание 5.1b

Переделать скрипт из задания 5.1a таким образом, чтобы, при запросе параметра,
отображался список возможных параметров.

Вывести информацию о соответствующем параметре, указанного устройства.

Пример выполнения скрипта:
$ python task_5_2b.py
Введите имя устройства: r1
Введите имя параметра (ios, model, vendor, location, ip): ip
10.255.0.1

Ограничение: нельзя изменять словарь london_co.

Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if.
'''

dev = input("Введите имя устройства r1/r2/sw1: ")
nam = input("Введите имя параметра (ios, model, vendor, location, ip): ")
london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}

print(london_co[dev][nam])
