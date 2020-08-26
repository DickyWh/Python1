# -*- coding: utf-8 -*-
'''
задание 7.2c
Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
  * имя исходного файла конфигурации
  * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

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
A = text[0]
B = text[1]
ignore = ['duplex', 'alias', 'Current configuration']
with open(A, 'r') as source, open(B, 'a') as dest:
    for line in source:
        if line.find(ignore[0]) is -1 and line.find(ignore[1]) is -1 and line.find(ignore[2]) is -1:
            dest.write(line)
            #print(line.strip('\n'))



