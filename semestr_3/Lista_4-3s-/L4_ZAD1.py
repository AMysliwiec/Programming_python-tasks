class QueueBaB(object):
    """
    A class that implements a queue using a Python list
    The start of the queue is stored at the top of the list
    """
    def __init__(self):
        self.list_of_items = []

    def isEmpty(self):
        """
        A method to check if a queue is empty.
        :return: True if queue is empty, if not - False
        """
        if not self.list_of_items:
            return True
        return False

    def enqueue(self, *items):
        """
        Method for adding an object to the queue.
        :param items: object/objects to add
        """
        for item in list(items):
            self.list_of_items.append(item)

    def dequeue(self):
        """
        Method for extracting an object from the queue.
        """
        return self.list_of_items.pop(0)

    def size(self):
        """
        :return: length of the queue
        """
        return len(self.list_of_items)

    def __str__(self):
        return str(self.list_of_items)


class QueueBaE(object):
    """
    A class that implements a queue using a Python list
    The start of the queue is stored at the end of the list
    """
    def __init__(self):
        self.list_of_items = []

    def isEmpty(self):
        """
        A method to check if a queue is empty.
        :return: True if queue is empty, if not - False
        """
        if not self.list_of_items:
            return True
        return False

    def enqueue(self, *items):
        """
        Method for adding an object to the queue.
        :param items: object/objects to add
        """
        for item in list(items):
            self.list_of_items.insert(0, item)

    def dequeue(self):
        """
        Method for extracting an object from the queue.
        """
        return self.list_of_items.pop()

    def size(self):
        """
        :return: length of the queue
        """
        return len(self.list_of_items)

    def __str__(self):
        return str(self.list_of_items)
