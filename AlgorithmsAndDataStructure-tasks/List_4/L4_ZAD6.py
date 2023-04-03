from L4_ZAD5 import UnorderedList, Node


class StackUsingUL(object):
    def __init__(self):
        self.items = UnorderedList()

    def is_empty(self):
        """
        A method to check if the stack is empty.
        """
        return self.items.isEmpty()

    def push(self, item):
        """
        The method places a new item on the stack.
        :param item: item to place
        """
        self.items.append(item)

    def pop(self):
        """
        The method pops the item off the stack.
        :return: popped element
        """
        if self.is_empty():
            raise IndexError("Stack is empty")

        return self.items.pop()

    def peek(self):
        """
        The method gives the value of the item on top of the stack without taking it off.
        :return: the top element of the stack
        """
        if self.is_empty():
            raise IndexError("Stack is empty")

        current = self.items.head
        while current.getNext() is not None:
            current = current.getNext()
        value = current.getData()
        return value

    def size(self):
        """
        :return: the number of items on the stack
        """
        return self.items.size()

    def __str__(self):
        return str(self.items)
