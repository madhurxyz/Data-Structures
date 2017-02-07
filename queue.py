#!python
from linkedlist import LinkedList

# enqueue - append to tail
# dequeue - remove from head
# peek - examine first


# class Queue(object):
#
#     def __init__(self, iterable=None):
#         """Initialize this queue and enqueue the given items, if any"""
#         self.queue = []
#         if iterable:
#             for item in iterable:
#                 self.enqueue(item)
#
#     def __repr__(self):
#         """Return a string representation of this queue"""
#         return 'Queue({})'.format(self.length())
#
#     #O(1)
#     def is_empty(self):
#         """Return True if this queue is empty, or False otherwise"""
#         if len(self.queue) == 0:
#             return True
#         return False
#
#     #O(1)
#     def length(self):
#         """Return the number of items in this queue"""
#         return len(self.queue)
#
#     #O(1)
#     def peek(self):
#         """Return the next item in this queue without removing it,
#         or None if this queue is empty"""
#         if self.is_empty():
#             return None
#         return self.queue[0]
#
#     #O(1)
#     def enqueue(self, item):
#         """Enqueue the given item into this queue"""
#         self.queue.append(item)
#
#     #O(1)
#     def dequeue(self):
#         """Return the next item and remove it from this queue,
#         or raise ValueError if this queue is empty"""
#         if self.is_empty():
#             raise ValueError
#         else:
#             return self.queue.pop(0)

class Queue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any"""
        self.queue = LinkedList()
        if iterable:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue"""
        return 'Queue({})'.format(self.length())

    #O(1)
    def is_empty(self):
        """Return True if this queue is empty, or False otherwise"""
        if self.queue.length() == 0:
            return True
        return False

    #O(1)
    def length(self):
        """Return the number of items in this queue"""
        return self.queue.length()

    #O(1)
    def peek(self):
        """Return the next item in this queue without removing it,
        or None if this queue is empty"""
        if self.is_empty():
            return None
        return self.queue.head.data

    #O(1)
    def enqueue(self, item):
        """Enqueue the given item into this queue"""
        self.queue.append(item)

    #O(n)
    def dequeue(self):
        """Return the next item and remove it from this queue,
        or raise ValueError if this queue is empty"""
        if self.is_empty():
            raise ValueError
        else:
            first_item = self.queue.head.data
            self.queue.delete(first_item)
            return first_item
