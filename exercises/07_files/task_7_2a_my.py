# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
      Скрипт не должен выводить команды, в которых содержатся слова,
      которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

ignore = ['duplex', 'alias', 'Current configuration']
'''

#f = open('config_sw1.txt')
#while True:
#    line = f.readline()
#    print(line.rstrip().strip('!'))
#    if not line:
#        break

from sys import argv
text = argv[1:]
text = ''.join(text)
ignore = ['duplex', 'alias', 'Current configuration', '!']
with open(text, 'r') as file:
    for line in file:
        if line.find(ignore[0]) is -1 and line.find(ignore[1]) is -1 and line.find(ignore[2]) is -1 and line.find(ignore[3]) is -1:
            print(line.strip('\n'))



