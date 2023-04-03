class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, new_next):
        self.next = new_next


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:  # jeśli usuwamy pierwszy element
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    # ------------------- SELF-ADDED METHODS -------------------------

    def append(self, item):
        """
        Method to add an item to the end of the list.
        :param item: object to add
        """
        current = self.head
        temp = Node(item)

        if self.isEmpty():
            self.add(item)
        else:
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(temp)

    def index(self, item):
        """
        The method gives a place on the list, which has a specific element -
        the element underneath self.head has an index 0.
        :param item: element, whose position is to be determined
        :return: item position on the list or None in the case of,
        when the chosen item is not on the list
        """
        index_pos = 0
        current = self.head

        while current is not None:
            if current.getData() == item:
                return index_pos
            else:
                current = current.getNext()
                index_pos += 1

        return None

    def insert(self, pos, item):
        """
        The method places a given element on the given position.
        Takes the position as arguments,
        on which to place the element and this element.
        :param pos: position on which to place the element
        :param item: element to place
        """
        temp = Node(item)
        current, current_pos, size = self.head, 0, self.size()

        if -size <= pos < 0:  # odczytanie indeksu ujemnego
            pos += size + 1

        if pos == 0:
            self.add(item)
        elif pos == size:
            self.append(item)
        elif not 0 <= pos < size:
            raise IndexError("Incorrect index")
        else:
            while current_pos != (pos - 1):
                current = current.getNext()
                current_pos += 1

            next_for_temp = current.getNext()
            temp.setNext(next_for_temp)
            current.setNext(temp)

    def pop(self, pos=-1):
        """
        The method removes an item from the list from the specific place.
        :param pos: optional; position .
        :return: deleted element
        """
        current, current_pos, size = self.head, 0, self.size()
        previous = None
        limes = size

        if self.isEmpty():
            raise IndexError("empty list, nothing to pop")
        if not abs(pos) <= limes:
            raise IndexError("Incorrect index")

        while current is not None:
            if current_pos == 0:
                if pos == -1 and size == 1:
                    self.head = previous
                    return current.getData()
                elif pos == 0:
                    self.head = current.getNext()
                    return current.getData()

            if current_pos in [pos, pos + size]:
                previous.setNext(current.getNext())
                return current.getData()

            previous = current
            current = current.getNext()
            current_pos += 1

    # ---------------------------------------------------------------

    def __str__(self):
        current = self.head
        li = []
        while current is not None:
            li.append(current.getData())
            current = current.getNext()
        s = ("elements in the list are [" + ', '.join(['{}'] * len(li)) + "]")
        return s.format(*li)
