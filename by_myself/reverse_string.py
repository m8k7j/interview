#!/usr/bin/env python
# coding=utf-8

"""
input_s = "terry ding is a good boy"
output_s = "yob doog a si gnid yrret"

"""


def reverse_string(input_s):
    li_s = list(input_s) #字符串转列表
    reverse_li = []
    reverse = ""
    for i in range(len(li_s)):
    #当用pop的时候会影响到原列表，
    #因此不能用 for i in li_s, 而是用长度
        reverse_li.append(li_s.pop())
    for j in reverse_li:
        reverse += j #列表转字符串
    return reverse


if __name__ == '__main__':
    input_s = "terry ding is a good boy"
    print reverse_string(input_s)
