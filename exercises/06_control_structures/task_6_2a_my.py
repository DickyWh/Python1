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

ip = input('Введите IP-адрес в формате х.х.х.х: ')
check = ip.count('.')
if check != 3:
    print('Неправильный IP-адрес. необходимо ввести три точки между числами')
else:
#проверка на наличие цифр в октетах
    ip = ip.strip().split('.')
    int1 = ip[0].isdigit()
    int2 = ip[1].isdigit()
    int3 = ip[2].isdigit()
    int4 = ip[3].isdigit()
    if int1 is not True and int2 is not True and int3 is not True and int4 is not True:
        print('Неправильный IP-адрес, вводите только числа')
    else:
#проверка на разрешенный диапазон цифр(0-255) в октетах
        ip_o1 = int(ip[0])
        ip_o2 = int(ip[1])
        ip_o3 = int(ip[2])
        ip_o4 = int(ip[3])
        allowed_range = list(range(0, 256))
        if ip_o1 not in allowed_range or ip_o2 not in allowed_range or ip_o3 not in allowed_range or ip_o4 not in allowed_range:
            print('Неправильный IP-адрес, разрешен только диапазон 0-255')
        else:
#основная проверка из задания 6.2
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




