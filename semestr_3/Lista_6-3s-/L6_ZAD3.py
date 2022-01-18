class LimitedBinHeap:

    def __init__(self, max_size):
        self.heap_list = [0]
        self.current_size = 0
        self.max_size = max_size

    def size(self):
        return self.current_size

    def is_empty(self):
        return self.current_size == 0

    def perc_up(self, index):
        while index // 2 > 0:
            if self.heap_list[index] < self.heap_list[index // 2]:
                tmp = self.heap_list[index // 2]
                self.heap_list[index // 2] = self.heap_list[index]
                self.heap_list[index] = tmp
            index //= 2

    def find_min(self):
        return self.heap_list[1]

    def min_child(self, index):
        if index * 2 + 1 > self.current_size:
            return index * 2
        else:
            if self.heap_list[index * 2] < self.heap_list[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1

    def perc_down(self, index):
        while (index * 2) <= self.current_size:
            smaller_child = self.min_child(index)
            if self.heap_list[index] > self.heap_list[smaller_child]:
                tmp = self.heap_list[index]
                self.heap_list[index] = self.heap_list[smaller_child]
                self.heap_list[smaller_child] = tmp
            index = smaller_child

    def del_min(self):
        min_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[-1]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return min_value

    def insert(self, k):

        if self.current_size < self.max_size:
            self.heap_list.append(k)
            self.current_size += 1
            self.perc_up(self.current_size)
        else:
            if self.find_min() > k:
                raise ValueError("Given value is too small")
            else:
                self.del_min()
                self.insert(k)

    def build_heap(self, build_list):

        size = len(build_list)
        if size > self.max_size:
            max_list = build_list[:self.max_size]
            self.build_heap(max_list)

            for i in build_list[self.max_size:]:
                self.insert(i)
        else:
            index = size // 2
            self.current_size = size
            self.heap_list = [0] + build_list[:]
            while index > 0:
                self.perc_down(index)
                index -= 1

    def __str__(self):
        return str(self.heap_list[1:])
