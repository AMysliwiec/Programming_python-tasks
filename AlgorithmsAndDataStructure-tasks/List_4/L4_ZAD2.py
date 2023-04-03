import time
import numpy as np
from L4_ZAD1 import QueueBaB, QueueBaE
import matplotlib.pyplot as plt


# ---------- FUNCTIONS THAT CHECK FOR N EXECUTIONS ---------------


def enqueue_times(n):
    BaB = QueueBaB()
    BaE = QueueBaE()

    start_BaB = time.time()
    for i in range(0, n):
        BaB.enqueue(i)
    end_BaB = time.time()
    time_BaB = end_BaB - start_BaB

    start_BaE = time.time()
    for i in range(0, n):
        BaE.enqueue(i)
    end_BaE = time.time()
    time_BaE = end_BaE - start_BaE

    return [time_BaB, time_BaE], [BaB, BaE]


def dequeue_times(n):
    BaB = enqueue_times(n)[1][0]
    BaE = enqueue_times(n)[1][1]

    start_BaB = time.time()
    for i in range(0, n):
        BaB.dequeue()
    end_BaB = time.time()
    time_BaB = end_BaB - start_BaB

    start_BaE = time.time()
    for i in range(0, n):
        BaE.dequeue()
    end_BaE = time.time()
    time_BaE = end_BaE - start_BaE

    return [time_BaB, time_BaE]


def enq_and_deq(n):
    BaB = QueueBaB()
    BaE = QueueBaE()

    start_BaB = time.time()
    for i in range(0, n):
        BaB.enqueue(i)
    for i in range(0, n):
        BaB.dequeue()
    end_BaB = time.time()
    time_BaB = end_BaB - start_BaB

    start_BaE = time.time()
    for i in range(0, n):
        BaE.enqueue(i)
    for i in range(0, n):
        BaE.dequeue()
    end_BaE = time.time()
    time_BaE = end_BaE - start_BaE

    return [time_BaB, time_BaE]


# ------------------ COMPARE AND PLOT -------------------------


def compare_enqueue(n):
    x = np.linspace(0, 20, 21)
    values_BaB = enqueue_times(n)[0][0] * x
    values_BaE = enqueue_times(n)[0][1] * x
    plt.plot(x, values_BaB, c="blue", label="BaB")
    plt.plot(x, values_BaE, c="red", label="BaE")
    plt.title("Comparison of enqueue methods")
    plt.xlabel("Constant function for n = {}".format(n))
    plt.ylabel("Time")
    plt.legend()
    plt.grid()
    plt.show()


def compare_dequeue(n):
    x = np.linspace(0, 20, 21)
    values_BaB = dequeue_times(n)[0] * x
    values_BaE = dequeue_times(n)[1] * x
    plt.plot(x, values_BaB, c="blue", label="BaB")
    plt.plot(x, values_BaE, c="red", label="BaE")
    plt.title("Comparison of dequeue methods")
    plt.xlabel("Constant function for n = {}".format(n))
    plt.ylabel("Time")
    plt.legend()
    plt.grid()
    plt.show()


def compare_both(n):
    x = np.linspace(0, 20, 21)
    values_BaB = enq_and_deq(n)[0] * x
    values_BaE = enq_and_deq(n)[1] * x
    plt.plot(x, values_BaB, c="blue", label="BaB")
    plt.plot(x, values_BaE, c="red", label="BaE")
    plt.title("Comparison of enqueue and dequeue methods")
    plt.xlabel("Constant function for n = {}".format(n))
    plt.ylabel("Time")
    plt.legend()
    plt.grid()
    plt.show()


# ----------------------------------------------------------------


def get_enqueue_times(n):
    single_times_BaB, single_times_BaE = [], []
    x = [x for x in range(0, n, 100)]
    for timer in x:
        times = enqueue_times(timer)[0]
        BaB_times = times[0]
        BaE_times = times[1]
        single_times_BaB.append(BaB_times)
        single_times_BaE.append(BaE_times)

    return [x, single_times_BaB, single_times_BaE]


def get_dequeue_times(n):
    single_times_BaB, single_times_BaE = [], []
    x = [x for x in range(0, n, 100)]
    for timer in x:
        times = dequeue_times(timer)
        BaB_times = times[0]
        BaE_times = times[1]
        single_times_BaB.append(BaB_times)
        single_times_BaE.append(BaE_times)

    return [x, single_times_BaB, single_times_BaE]


def compare_time(n, name):
    if name == "enqueue":
        data = get_enqueue_times(n)
        tlt = "Comparison of enqueue method"
    elif name == "dequeue":
        data = get_dequeue_times(n)
        tlt = "Comparison of dequeue method"

    x = data[0]
    values_BaB = data[1]
    values_BaE = data[2]
    plt.plot(x, values_BaB, c="blue", label="BaB")
    plt.plot(x, values_BaE, c="red", label="BaE")

    xaxis = [0, x[-1]]  # wykresy liniowe
    plt.plot(xaxis, [0, values_BaB[-1]])
    plt.plot(xaxis, [0, values_BaE[-1]])

    plt.title(tlt)
    plt.xlabel("Number of elements")
    plt.ylabel("Time")
    plt.legend()
    plt.grid()
    plt.show()


# ---------------- SAME N SIMULATION -------------------------


def get_both_times(n):
    single_times_BaB, single_times_BaE = [], []
    x = [x for x in range(0, n, 100)]
    for timer in x:
        times = enq_and_deq(n)
        BaB_times = times[0]
        BaE_times = times[1]
        single_times_BaB.append(BaB_times)
        single_times_BaE.append(BaE_times)

    return [x, single_times_BaB, single_times_BaE]


def compare_both_same_times(n):
    data = get_both_times(n)
    x = data[0]
    values_BaB = data[1]
    values_BaE = data[2]
    plt.plot(x, values_BaB, c="blue", label="BaB")
    plt.plot(x, values_BaE, c="red", label="BaE")
    plt.title("Comparison of enqueue and dequeue methods")
    plt.xlabel("Number of executions")
    plt.ylabel("Time")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == '__main__':

    # LINEAR SPECULATION
    compare_enqueue(10000)
    compare_dequeue(10000)
    compare_both(10000)

    # COMPARING REAL TIME
    compare_time(10000, "enqueue")
    compare_time(10000, "dequeue")

    compare_both_same_times(10000)
