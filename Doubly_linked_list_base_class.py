#!/usr/bin/env python
# coding: utf-8

### Doubly linked list base class

class  _DoublyLinkedListBase:
    ''' base class representating doubly linked list '''
    class _Node:
        __slot__='_data','_next','_previous'
        def __init__(self,data,next,previous):
            self._data=data
            self._next=next
            self._previous=previous
    def __init__(self):
        self._frontEnd=self._Node(None,None,None)
        self._rareEnd=self._Node(None,None,None)
        self._frontEnd._next=self._rareEnd
        self._rareEnd._previous=self._frontEnd
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def _insertBetween(self,data,predecessor,successor):
        newNode=self._Node(data,predecessor,successor)
        predecessor._next=newNode
        successor._previous=newNode
        size +=1
        return newNode
    def _deleteNode(self,node):
        predecessor=node._previous
        successor=node._next
        predecessor._next=successor
        successor._previous=predecessor
        element=node._data
        node._previous=Node._next=node._data=None
        size -=1
        return element

