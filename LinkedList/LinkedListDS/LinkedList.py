__author__ = 'Zach'

from LinkedListDS.Node import Node

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.counter = 0

    def traverseList(self):
        """ O(n) complexity """
        actualNode = self.head

        while actualNode is not None:
            print("%d " % actualNode.data)
            actualNode = actualNode.nextNode

    def insertStart(self, data):
        """O(1) Complexity"""

        self.counter += 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def size(self):
        """O(1) Complexity instead of O(n)"""
        return self.counter

    def insertEnd(self,data):
        """O(n) complexity"""
        if self.head is None:
            self.insertStart(data)
            return
        self.counter += 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def remove (self, data):
        """O(1) if we are at head, O(n) in general"""
        self.counter -= 1

        if self.head:
            if data == self.head.data:
                self.head = self.head.nextNode
            else:
                self.head.remove(data, self.head)