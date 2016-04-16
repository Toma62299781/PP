import math

li = [1, 2, 3, 4, 5, 6.58, 7, 8, 9]

def BinarySearch(x, li):
    i = 0
    j = len(li) - 1
    while i < j:
        m = (i + j) / 2
        if x > li[m]:
            i = m + 1
        else:
            j = m
    if x == li[i]:
        location = i
    else:
        location = -1
    print location


BinarySearch(6.58, li)