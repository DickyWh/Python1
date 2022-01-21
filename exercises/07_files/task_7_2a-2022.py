# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

filename = argv[1]

with open(filename) as f:
    for line in f:
        words = line.split()
        words_intersect = set(words) & set(ignore)
        if not line.startswith("!") and not words_intersect:
            print(line.rstrip())

#from sys import argv
#text = argv[1]
#text = ''.join(text)
#ignore = ['duplex', 'alias', 'Current configuration', '!']

#with open(text, 'r') as f:
#    for line in f:
#        if line.find(ignore[0]) is -1 and line.find(ignore[1]) is -1 and line.find(ignore[2]) is -1 and line.find(ignore[3]) is -1:
#                     print(line.strip('\n'))
