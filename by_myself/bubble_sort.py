#!/usr/bin/env python
# coding=utf-8

init = [9,5,4,3,7,6]

def bubble_sort(init):
    """
    第一个数与后面一个数相比，如果小了，就换位置
    第一个遍历可以把最大的数排在最后
    第n个遍历就可以排序
    """
    length = len(init)
    for i in range(length):
        for j in range(i+1,length):
            if init[i]>init[j]:
                init[i],init[j]=init[j],init[i]
    return init


if __name__ == '__main__':
    result = bubble_sort(init)
    for i in result:
        print i


