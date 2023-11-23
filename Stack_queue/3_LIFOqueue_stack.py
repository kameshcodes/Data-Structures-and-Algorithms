"""Create a fixed Size Stack Using LIFOQUEUE"""
from queue import LifoQueue
stack2 = LifoQueue(maxsize=3)

print(stack2.qsize)

stack2.put('a')
stack2.put('b')
stack2.put('c')
stack2.put('d')

print("Full : ", stack2.full())
print("Size : ", stack2.qsize())

print('\nElement popped from stack')
print(stack2.get())
print(stack2.get())
print(stack2.get())
print(stack2.get())
print("\nEmpty", stack2.empty())