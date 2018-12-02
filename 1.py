#! /usr/bin/python


freq_list = list()
with open('input/1.input') as fp:
    line = fp.readline()
    while line:
        freq_list.append(line)
        line = fp.readline()
fp.close()

initial = 0
for freq in freq_list:
    if '+' in freq:
        initial = initial + int(freq[1:])
    else:
        initial = initial - int(freq[1:])
print initial

# testing
#freq_list=['+3', '+3', '+4', '-2', '-4']
#freq_list=['-6', '+3', '+8', '+5', '-6']
#freq_list=['+7', '+7', '-2', '-7', '-4']

from itertools import cycle
fup=list()
initial = 0
fup.append(initial)
freq_cir_list = cycle(freq_list)

for freq in freq_cir_list:
    if '+' in freq:
        initial = initial + int(freq[1:])
    else:
        initial = initial - int(freq[1:])
    if initial in fup:
        print initial
        break
    else:
        fup.append(initial)
