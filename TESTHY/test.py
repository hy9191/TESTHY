#!/user/bin/env python
# -*- coding:utf-8 -*-

list_a = []
for i in range(1,4):
    list_a.append(i**2)
print(list_a)

list_a1 =[i**2 for i in range(1,4)]
print(list_a1)

list_a2 = []
for i in range(1,4):
    for j in range(1,4):
        list_a2.append(i*j)
print(list_a2)

list_a3 = [i*j for i in range(1,4) for j in range (1,4)]
print(list_a3)