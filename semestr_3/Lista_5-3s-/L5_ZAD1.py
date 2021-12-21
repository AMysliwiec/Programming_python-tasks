import numpy as np
from scipy import linalg
import os
import random
import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math


def linear_solve(n):
    A = np.array([[random.randint(-100, 100) for _ in range(n)] for _ in range(n)])
    B = np.array([random.randint(-100, 100) for _ in range(n)])

    return A, B


def time_check_and_save(list_of_data, file_name):
    times = []
    for num in list_of_data:
        A, B = linear_solve(num)
        start = time.time()
        linalg.solve(A, B)
        end = time.time()
        times.append(end - start)

    file = open(file_name, 'w')
    file.write(str(times))
    file.close()


def get_times(list_of_data, file_name):
    if not os.path.exists(file_name):
        time_check_and_save(list_of_data, file_name)

    file = open(file_name, 'r')
    times = eval(file.read())
    return times


def average(log_list):  # Funkcja liczy średnią arytmetyczną z listy, przyda się w szacowaniu przybliżenia b
    length, log_sum = 0, 0
    for num in log_list:
        if num is not None:
            length += 1
            log_sum += num
    return log_sum / length


def doubling_hypothesis(x_tab, y_tab):
    ratio = [None] * len(y_tab)
    for i in range(1, len(y_tab)):
        if y_tab[i - 1] != 0:
            ratio[i] = y_tab[i] / y_tab[i - 1]
        else:
            ratio[i] = 0
    lratio = [None]
    for val in ratio:
        if val:
            lratio.append(math.log(val, 2))
        else:
            lratio.append(None)

    print('\nN \t T \t \t \t Ratio \t \t \t Log')
    for i in range(len(y_tab)):
        print("{} \t {} \t {} \t {}".format(x_tab[i], y_tab[i], ratio[i], lratio[i]))

    average_b = average(lratio)
    average_a = a = y_tab[-2] / (x_tab[-2] ** average_b)

    print('\na: \t {} \nb: \t {}'.format(average_a, average_b))

    return average_a, average_b


def plot_results(n, filename):
    """
    results of doubling hypothesis
    """
    double_data_1 = [2 ** (n + i) for i in range(1, 6)]
    doubling_times = get_times(double_data_1, filename)

    data = doubling_hypothesis(double_data_1, doubling_times)
    plt.scatter(double_data_1, doubling_times, color='red', label='Results')
    plt.plot(range(1, 2 ** (5 + n)), [data[0] * i ** data[1] for i in range(1, 2 ** (5 + n))],
             label='approximate curve')
    plt.xlabel("Number of unknowns")
    plt.ylabel("Execution time [s]")
    plt.legend(loc='upper left')
    plt.title("Time of executions depending on the number of unknowns")
    plt.show()


def func(x, a, power=2):
    return a * x ** power


def plot_with_fitted_curve(x, y, popt):
    x2 = np.arange(1, x[-1])

    plt.plot(x, y, 'rp', label="Results")
    plt.plot(x2, func(x2, *popt), label="Fitted curve")
    plt.xlabel("Number of unknownss")
    plt.ylabel("Execution time [s]")
    plt.legend(loc='upper left')
    plt.title("Time of executions depending on the number of unknowns")
    plt.show()


def plot_with_fitted_curve_log(x, y, popt):
    x2 = np.arange(10 ** 2, x[-1])

    plt.loglog(x, y, 'rp', label="Results")
    plt.loglog(x2, func(x2, *popt), label="Fitted curve")
    plt.xlabel("Number of unknowns")
    plt.ylabel("Execution time [s]")
    plt.legend(loc='upper left')
    plt.title("Time of executions depending on the number of unknowns \n - logarithmic scale")
    plt.show()


if __name__ == '__main__':
    trial_data = [400 * i for i in range(1, 11)]
    trial_times = get_times(trial_data, 'trial.txt')

    plt.scatter(trial_data, trial_times)
    plt.xlabel("Number of unknowns")
    plt.ylabel("Execution time [s]")
    plt.title("Trial analysis oh the execution time")
    plt.show()

    plt.loglog(trial_data, trial_times, 'bo')
    plt.xlabel("Number of unknowns")
    plt.ylabel("Execution time [s]")
    plt.title("Trial analysis oh the execution time - logarithmic scale")
    plt.show()

    plot_results(7, 'data_1.txt')
    plot_results(8, 'data_2.txt')

    popt, pcov = curve_fit(func, trial_data, trial_times)
    plot_with_fitted_curve(trial_data, trial_times, popt)
    plot_with_fitted_curve_log(trial_data, trial_times, popt)

    # TRY FOR ANOTHER LIST

    another_try = [1000 * i for i in range(1, 9)]
    another_times = get_times(another_try, 'another.txt')

    popt_2, pcov_2 = curve_fit(func, another_try, another_times)
    plot_with_fitted_curve(another_try, another_times, popt_2)
    plot_with_fitted_curve_log(another_try, another_times, popt_2)
