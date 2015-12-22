__author__ = 'Zach'

from Stack import Stack

stack = Stack()

stack.push('A')
stack.push('B')
stack.push('C')

print(stack.pop())
print(stack.pop())
print(stack.size())
print(stack.pop())
print(stack.size())