"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
import singly_linked_list

myList = singly_linked_list.LinkedList()
myList.headval = singly_linked_list.Node("Apple")

node2 = singly_linked_list.Node("Banana")
node3 = singly_linked_list.Node("Carrot")
node4 = singly_linked_list.Node("Durian")


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        print(self.size)

    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1
        print(self.storage)

    def dequeue(self):
        self.storage.pop(0)
        self.size -= 1
        print(self.storage)


myQueue = Queue()

myQueue.enqueue(3)
myQueue.enqueue('f')
myQueue.enqueue("*")


myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()
