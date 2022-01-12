#-*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
    Если адрес был введен неправильно, запросить адрес снова.

    Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ip = input('Введите IP-адрес в формате х.х.х.х: ')

ip_correct = False

while not ip_correct:
    if ip.count('.') != 3:
        print('Неправильный IP-адрес. необходимо ввести три точки между числами')
#проверка на наличие цифр в октетах
    elif ip.strip().split('.')[0].isdigit() is False or ip.strip().split('.')[1].isdigit() is False or ip.strip().split('.')[2].isdigit() is False or ip.strip().split('.')[3].isdigit() is False:
        print('Неправильный IP-адрес, вводите только числа')
#проверка на разрешенный диапазон цифр(0-255) в октетах
    elif int(ip.strip().split('.')[0]) not in list(range(0, 256)) or int(ip.strip().split('.')[1]) not in list(range(0, 256)) or int(ip.strip().split('.')[2]) not in list(range(0, 256)) or int(ip.strip().split('.')[3]) not in list(range(0, 256)):
        print('Неправильный IP-адрес, разрешен только диапазон 0-255')
#основная проверка из задания 6.2
    else:
        ip = ip.strip().split('.')
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
        ip_correct = True
        continue
    ip = input('Введите IP-адрес ещё раз: ')





