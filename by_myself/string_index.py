#!/usr/bin/env python
# coding=utf-8

"""
input_str = "terry ding is a good boy"
ouput_str = “t1e1r2y1 d1i1n1g1 i1s1 a1 g1o2d1 b1o1y1"
"""

def string_index(input_str):
    length = len(input_str)
    count = 1
    initial_pos = 0
    cur_pos = 1
    result = ""
    while cur_pos < length:
        if input_str[cur_pos] == input_str[initial_pos]:
            count += 1
            cur_pos += 1
            if cur_pos == length:  #解决末尾一直相同的问题
                result += input_str[initial_pos]
                result += str(count)

        else:
            result += input_str[initial_pos]
            result += str(count)
            #当出现不同的时侯也就是重新计算
            # 计数为初值
            # 新的字符串指针赋初值
            count = 1
            initial_pos = cur_pos
            cur_pos += 1
    return result


if __name__ == '__main__':

    input_str = "tteeerrrryyisaaggoodddddd"
    result = string_index(input_str)
    print result



