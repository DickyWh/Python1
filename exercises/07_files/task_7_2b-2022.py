# -*- coding: utf-8 -*-
'''
Задание 7.2b
Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

  При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
  Строки, которые начинаются на '!' отфильтровывать не нужно.

  Ограничение: Все задания надо выполнять используя только пройденные темы.

ignore = ['duplex', 'alias', 'Current configuration']
'''

#f = open('config_sw1.txt')
#while True:
#    line = f.readline()
#    print(line.rstrip().strip('!'))
#    if not line:
#        break

#from sys import argv
#text = argv[1:]
#text = ''.join(text)
#ignore = ['duplex', 'alias', 'Current configuration']
#with open(text, 'r') as source, open('config_sw1_cleared.txt', 'w') as dest:
#    for line in source:
#        if line.find(ignore[0]) is -1 and line.find(ignore[1]) is -1 and line.find(ignore[2]) is -1:
#            dest.write(line)
#print(line.strip('\n'))


from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

src_file, dst_file = argv[1], "config_sw1_cleared.txt"

#with open(src_file) as src, open(dst_file, 'w') as dst:
#    for line in src:
#        skip_line = False
#        for ignore_word in line:
#            if ignore_word in line:
#                skip_line = True
#                break
#        if not line.startswith("!") and not skip_line:
#            dst.write(line)

# вариант решения с for/else
with open(src_file) as src, open(dst_file, 'w') as dst:
    for line in src:
        for ignore_word in ignore:
            if line.startswith("!") or ignore_word in line:
                break
        else:
            dst.write(line)

