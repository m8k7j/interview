#!/usr/bin/env python
# coding=utf-8


class BTree(object):
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

    def insert_left(self, item):
        if not self.left_child:
            self.left_child = BinaryTree(item)
        else:
            t = self.left_child
            self.left_child = BinaryTree(item)
            self.left_child.left_child = t

    def insert_right(self, item):
        if not self.right_child:
            self.right_child = BinaryTree(item)
        else:
            t = self.right_child
            self.right_child = BinaryTree(item)
            self.right_child.right_child = t

def create_tree(init):
    root = BTree('a')
    for i in init:
        root.left_child(i)
        root.right_child()

