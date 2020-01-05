#!/usr/bin/env python
# encoding: utf-8

class ListStack(object):
    def __init__(self):
        self._item = []
    
    def push(self,value):
        self._item.append(value)
    
    def pop(self):
        return self._item.pop()


if __name__ == '__main__':
    stack = ListStack()
    stack.push('1')
    stack.push('2')
    assert stack.pop() == '2'

