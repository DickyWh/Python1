# -*- coding: utf-8 -*-
'''
Задание 7.2

Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt:
- имя файла передается как аргумент скрипту

Скрипт должен возвращать на стандартный поток вывода команды из переданного
конфигурационного файла, исключая строки, которые начинаются с '!'.

Между строками не должно быть дополнительного символа перевода строки.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
from sys import argv

filename = argv[1]

with open(filename) as f:
    for line in f:
        if not line.startswith("!"):
            print(line.rstrip())

#from sys import argv
#text = argv[1]
#text = ''.join(text)

#with open(text, 'r') as f:
#    for line in f:
#        if line.find("!") is -1:
#            print(line.strip('\n'))
