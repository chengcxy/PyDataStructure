#!/usr/bin/env python
# encoding: utf-8

class Node(object):
    def __init__(self,value,next=None):
        self.value = value
        self.next = next



class LinkedListStack(object):
    def __init__(self):
        self.top_node = None


    def push(self,value):
        node = Node(value)
        node.next = self.top_node
        self.top_node = node


    def pop(self):
        if self.top_node:
            value = self.top_node.value
            self.top_node = self.top_node.next
            return value








if __name__ == '__main__':
    linked_list_stack = LinkedListStack()
    linked_list_stack.push(1)
    linked_list_stack.push(2)
    assert linked_list_stack.pop() == 2

