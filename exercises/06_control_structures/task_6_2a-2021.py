# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ip = input('Введите IP адрес в формае х.х.х.х: ')

octets = ip.split(".")
correct_ip = len(octets) == 4

for i in octets:
    correct_ip = i.isdigit() and 0 <= int(i) <= 255 and correct_ip

if correct_ip:
    if 1 <= int(octets[0]) <= 223:
        print("unicast адрес")
    elif 224 <= int(octets[0]) <= 239:
        print('multicast адрес')
    elif ip == '0.0.0.0':
        print('unassigned адрес')
    elif ip == '255.255.255.255':
        print('local broadcast адрес')
    else:
        print('unused')
else:
    print('неправильный адрес')
