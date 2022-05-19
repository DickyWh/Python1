#-*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
    Если адрес был введен неправильно, запросить адрес снова.

    Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
while True:
    ip = input('Введите IP адрес в формае х.х.х.х: ')
    octets = ip.split(".")
    correct_ip = len(octets) == 4

    for i in octets:
        correct_ip = i.isdigit() and 0 <= int(i) <= 255 and correct_ip

    if correct_ip:
        break
    print("Непрвильный IP-адрес")

if 1 <= int(octets[0]) <= 223:
    print("unicast адрес")
elif 224 <= int(octets[0]) <= 239:
    print('multicast адрес')
elif ip == '0.0.0.0':
    print('unassigned адрес')
elif ip == '255.255.255.255':
    print('local broadcast адрес')
else:
    print('неправильный адрес')
