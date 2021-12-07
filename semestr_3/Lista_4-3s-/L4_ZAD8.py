from L4_ZAD5 import UnorderedList, Node
import time
import matplotlib.pyplot as plt


def append_times(n):
    python_list = []
    un_list = UnorderedList()

    start_python = time.time()
    for i in range(0, n):
        python_list.append(n)
    end_python = time.time()
    time_python = end_python - start_python

    start_un = time.time()
    for i in range(0, n):
        un_list.append(i)
    end_un = time.time()
    time_un = end_un - start_un

    return [time_python, time_un]


def insert_times(n):
    python_list = []
    un_list = UnorderedList()

    start_python = time.time()
    for i in range(0, n):
        python_list.insert(0, i)
    end_python = time.time()
    time_python = end_python - start_python

    start_un = time.time()
    for i in range(0, n):
        un_list.insert(0, i)
    end_un = time.time()
    time_un = end_un - start_un

    return [time_python, time_un]


def pop_times(n):
    python_list = [0 for i in range(0, n)]
    un_list = UnorderedList()
    for i in range(0, n):
        un_list.add(i)

    start_python = time.time()
    for i in range(n):
        python_list.pop()
    end_python = time.time()
    time_python = end_python - start_python

    start_un = time.time()
    for i in range(n):
        un_list.pop()
    end_un = time.time()
    time_un = end_un - start_un

    return [time_python, time_un]


def experiment(n):
    python_list = []
    un_list = UnorderedList()

    start_python = time.time()
    for i in range(0, n):
        python_list.append(n)
        python_list.insert(0, i)
        python_list.pop()
    end_python = time.time()
    time_python = end_python - start_python

    start_un = time.time()
    for i in range(0, n):
        un_list.append(i)
        un_list.insert(0, i)
        un_list.pop()
    end_un = time.time()
    time_un = end_un - start_un

    return [time_python, time_un]


def compare(n, name):
    """
    function shows the results using a graph
    :param n: number of elements
    :param name: determine what function we want to check
    """
    x = [i for i in range(n)]
    values_python, values_un = [], []

    for timer in range(n):

        if name == 'pop':
            data = pop_times(n)
            ttl = 'Comparison of pop method'
        elif name == 'insert':
            data = insert_times(n)
            ttl = 'Comparison of insert method'
        elif name == 'append':
            data = append_times(n)
            ttl = 'Comparison of append method'
        elif name == 'experiment':  # na później :)
            data = experiment(n)
            ttl = 'Comparison of the three methods'

        values_python.append(data[0])
        values_un.append(data[1])
    plt.scatter(x, values_python, c="blue", label="python")
    plt.scatter(x, values_un, c="red", label="unordered")
    plt.title(ttl)
    plt.xlabel("Number of elements")
    plt.ylabel("Time")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == '__main__':

    print("CHECKING APPEND")
    for i in range(5):
        check = append_times(2000)
        print("Time for python list: {}".format(check[0]) + "\n" + "Time for unrdered list: {}".format(check[1]) + "\n")

    print("CHECKING INSERT")
    for i in range(5):
        check = append_times(2000)
        print("Time for python list: {}".format(check[0]) + "\n" + "Time for unrdered list: {}".format(check[1]) + "\n")

    print("CHECKING POP")
    for i in range(5):
        check = append_times(2000)
        print("Time for python list: {}".format(check[0]) + "\n" + "Time for unrdered list: {}".format(check[1]) + "\n")

    print("PLOTS")

    compare(100, 'append')
    compare(100, 'insert')
    compare(100, 'pop')
    compare(100, 'experiment')


