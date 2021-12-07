from L4_ZAD5 import UnorderedList, Node


class DequeueUsingUL(object):

    def __init__(self):
        self.items = UnorderedList()

    def is_empty(self):
        """
        A method to check if the queue is empty.
        """
        return self.items.isEmpty()

    def add_left(self, item):
        """
        The method adds an item to the queue on the left.
        :param item: the item to be added
        """
        self.items.add(item)

    def add_right(self, item):
        """
        The method adds an item to the queue on the right.
        :param item: the item to be added
        """
        self.items.append(item)

    def remove_left(self):
        """
        The method removes the element from the queue on the left.
        :return: removed item
        """
        if self.is_empty():
            raise IndexError("Queue is empty")

        return self.items.pop(0)

    def remove_right(self):
        """
        The method removes the element from the queue on the left.
        :return: removed item
        """
        if self.is_empty():
            raise IndexError("Queue is empty")

        return self.items.pop()

    def size(self):
        """
        :return: the number of items in the queue
        """
        return self.items.size()

    def __str__(self):
        return str(self.items)
