#!/usr/bin/env python
# coding=utf-8

class Node(object):
    def __init__(self, data):
        self.data = data
        self._next = None


def create_list():
    head = Node(1)
    p = head
    for i in range(2, 7):
        p._next=Node(i)
        p = p._next
    return head


def reverse_list (head):
    p = head

    while p._next:
        q = p._next
        p._next = q._next
        q._next = head     #q是以后的头部
        head = q
    return head

def print_list(head):
    p = head
    while p:
        print p.data
        p = p._next



if __name__ == '__main__':
    node = Node(1)
    head = create_list()
    reverse = reverse_list(head)
    print_list(reverse)





