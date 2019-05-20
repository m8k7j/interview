#!/usr/bin/env python
# coding=utf-8

"""
最大子串
input_str = "abddferrsssfffflllllllll"
output = (8,l,15)
"""

def max_string(input_str):
    length = len(input_str)
    init_pos = 0
    cur_pos = 1
    count = 1
    max_count = 0
    while cur_pos < length:
        if input_str[init_pos] == input_str[cur_pos]:
            count += 1
            cur_pos += 1
            if max_count < count:
                max_count = count
                index = cur_pos - max_count + 1
        else:
            count = 1
            init_pos = cur_pos
            cur_pos += 1
    return (count, input_str[index], index)

if __name__ == '__main__':
    input_str = "abddferrsssfffllllll"
    print max_string(input_str)
