#!/usr/bin/env python
# coding=utf-8

"""
有number个button, button可以开可以关，每按一次转换一次操作
现在先按 2n 的顺序依次按button
2, 4, 6,... 2n各按一次
3, 6, 9,... 3n各按一次
...
100n 各按一次
最后灯的状态
"""
size = 10
light = [0 for i in range(size)]

def switch_light(item):
    if item == 0:
        return 1
    else:
        return 0


def status(light):
    for i in range(2, size+1):
        for j in range(i, size+1, i):
            #前面二层循环是为了得到2n, 3n,4n
            #i 是2,3,4
            #range(i, size+1,i)可以得到2,4,6,
            #3,6,9
            for k in range(1, size+1):
            #最后一层是原始的字符串
                if j==k:
                    light[k-1]=switch_light(light[k-1])
    return light

if __name__ == '__main__':
    result = status(light)
    for i in result:
        print i
