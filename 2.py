#! /usr/bin/python


line_list = list()
with open('input/2.input') as fp:
    line = fp.readline()
    while line:
        line_list.append(line)
        line = fp.readline()
fp.close()

#line_list=["abcdef","bababc","abbcde","abcccd","aabcdd","abcdee","ababab"]
dict_list=list()
for line in line_list:
    dict = {}
    for n in line:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    dict_list.append(dict)

count_2=0
count_3=0

for dict in dict_list:
    if 2 in dict.values():
        count_2+=1
    if 3 in dict.values():
        count_3+=1

print count_2*count_3

import difflib
for line in line_list:
    for sline in line_list:
        output_list = [li for li in difflib.ndiff(line, sline) if li[0] != ' ']
        if len(output_list) ==2:
            print output_list,line,sline