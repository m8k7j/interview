#!/usr/bin/env python
# coding=utf-8


"""
删除一个列表的重复元素
li = [1,2,3,3,4,4,3,4,7]
li_out = [1,2,3,4,7]
"""

init = [1,2,3,4,5,4,3,7,3,4,7]

def delete_redundant(li):
    length = len(li)
    result = []
    for i in init:
        if i not in result:  #新建一个列表，看值在不在列表里
            result.append(i)
    return result

if __name__ == '__main__':
    result = delete_redundant(init)
    for i in result:
        print i


