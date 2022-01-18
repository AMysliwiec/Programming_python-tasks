class LimitedBinHeap:

    def __init__(self, limit):
        self.heap_list = [0]
        self.current_size = 0
        self.limit = limit

    def size(self):
        return self.current_size

    def is_empty(self):
        return self.current_size == 0

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i //= 2

    def find_min(self):
        return self.heap_list[1]

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def perc_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    def del_min(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[-1]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return retval

    def insert(self, k):

        if self.current_size < self.limit:
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
        if size <= self.limit:
            i = size // 2
            self.current_size = size
            self.heap_list = [0] + build_list[:]
            while i > 0:
                self.perc_down(i)
                i -= 1
        else:
            limit_list = build_list[:self.limit]
            self.build_heap(limit_list)

            for k in build_list[self.limit:]:
                self.insert(k)

    def __str__(self):
        return str(self.heap_list[1:])
