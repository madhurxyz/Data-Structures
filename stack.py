#!python
from linkedlist import LinkedList
# push to end
# pop from end
# peek end

# class Stack(object):
#
#     def __init__(self, iterable=None):
#         """Initialize this stack and push the given items, if any"""
#         self.stack = []
#         pass
#         if iterable:
#             for item in iterable:
#                 self.push(item)
#
#     def __repr__(self):
#         """Return a string representation of this stack"""
#         return 'Stack({})'.format(self.length())
#
#     #O(1)
#     def is_empty(self):
#         """Return True if this stack is empty, or False otherwise"""
#         if len(self.stack) == 0:
#             return True
#         return False
#
#     #O(1)
#     def length(self):
#         """Return the number of items in this stack"""
#         return len(self.stack)
#
#     #O(1)
#     def peek(self):
#         """Return the top item on this stack without removing it,
#         or None if this stack is empty"""
#         if self.is_empty():
#             return None
#         return self.stack[self.length() - 1]
#
#     #O(1)
#     def push(self, item):
#         """Push the given item onto this stack"""
#         self.stack.append(item)
#
#     #O(1)
#     def pop(self):
#         """Return the top item and remove it from this stack,
#         or raise ValueError if this stack is empty"""
#         if self.is_empty():
#             raise ValueError
#         else:
#             return self.stack.pop()

class Stack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any"""
        self.stack = LinkedList()
        pass
        if iterable:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack"""
        return 'Stack({})'.format(self.length())

    #O(1)
    def is_empty(self):
        """Return True if this stack is empty, or False otherwise"""
        if self.stack.length() == 0:
            return True
        return False

    #O(1)
    def length(self):
        """Return the number of items in this stack"""
        return self.stack.length()

    #O(1)
    def peek(self):
        """Return the top item on this stack without removing it,
        or None if this stack is empty"""
        if self.is_empty():
            return None
        return self.stack.tail.data

    #O(1)
    def push(self, item):
        """Push the given item onto this stack"""
        self.stack.append(item)

    #O(n)
    def pop(self):
        """Return the top item and remove it from this stack,
        or raise ValueError if this stack is empty"""
        if self.is_empty():
            raise ValueError
        else:
            first_item = self.stack.tail.data
            self.stack.delete(first_item)
            return first_item
