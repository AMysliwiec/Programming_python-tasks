import numpy as np
import os
import random
import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

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
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.perc_down(1)
        return retval

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)

    def buildHeap(self, build_list):
        i = len(build_list) // 2
        self.current_size = len(build_list)
        self.heap_list = [0] + build_list[:]
        while i > 0:
            self.perc_down(i)
            i -= 1

    def __str__(self):
        txt = "{}".format(self.heap_list[1:])
        return txt


# -------------- SORT FUNCTION --------------------


def sort_heap(data_list):
    heap = BinHeap()
    heap.buildHeap(data_list)
    return [heap.del_min() for _ in range(len(data_list))]


# -------------- PART FOR ANALYSIS ---------------


def random_sort_time(n):
    random_data = [random.randint(-100, 100) for _ in range(n)]
    start = time.process_time()
    sort_heap(random_data)
    end = time.process_time()
    time_data = end - start
    return time_data


def time_check_and_save(n_list, file_name):
    times = []
    for num in n_list:
        times.append(random_sort_time(num))
    file = open(file_name, 'w')
    file.write(str(times))
    file.close()


def get_times(list_of_data, file_name):
    if not os.path.exists(file_name):
        time_check_and_save(list_of_data, file_name)

    file = open(file_name, 'r')
    times = eval(file.read())
    return times


def func(n, a, b):
    return a * n * np.log(n) + b


def plot_hypothesis(x, y, func, popt):
    x2 = np.arange(1, x[-1])
    plt.plot(x, y, 'rp', label="Results")
    plt.plot(x2, func(x2, *popt), label="Fitted curve")
    plt.xlabel("Number of elements")
    plt.ylabel("Execution time [s]")
    plt.legend(loc='upper left')
    plt.title("Time of executions depending on the heap size")
    plt.show()


if __name__ == "__main__":

    trial_data = [10000 * n for n in range(1, 6)]
    trial_times = get_times(trial_data, 'trial.txt')

    popt, pcov = curve_fit(func, trial_data, trial_times)
    plot_hypothesis(trial_data, trial_times, func, popt)

    trial_data2 = [2000 * n for n in range(1, 20)]
    trial_times2 = get_times(trial_data2, 'trial2.txt')

    popt2, pcov2 = curve_fit(func, trial_data2, trial_times2)
    plot_hypothesis(trial_data2, trial_times2, func, popt2)

