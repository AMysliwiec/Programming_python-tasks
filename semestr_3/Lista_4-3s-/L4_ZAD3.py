from L4_ZAD1 import QueueBaE
import random
import matplotlib.pyplot as plt

"""
### Bistro
Z uwagi na panujące obostrzenia, w pewnym bistro jest określona maksymalna liczba osób, która może przebywać 
jednocześnie w lokalu. Symulacje przeprowadzane są przy założeniu, iż restrykcje się zmieniają oraz pozostaje 
dysproporcja w tempie pracy poszczególnych kasjerek. Czas obsługi konkretnego klienta również jest zróżnicowany 
(np. nakłada większą ilość jedzenia). 
Z zeszłorocznych danych również wiemy, że bistro odwiedza od 8 do 15 osób na godzinę.

Każdy klient, który w godzinę zamknięcia bistro stoi w kolejce poza lokalem, niestety nie może zostać obsłużony.
Ile średnio osób dziennie, nie zostaje obsługiwanych?
"""


class Bistro:
    def __init__(self, restriction, faster_service_pace):
        """
        :param restriction: how many clients can wait inside, pandemic times :(
        :param faster_service_pace: client can be serviced by different cashiers
        True - faster, False - slower cashier!
        """
        self.clients = None
        self.current_client = None
        self.open_hours = 360
        self.full_queue_inside = False
        self.restricted_amount_of_clients = restriction
        self.faster_service_pace = faster_service_pace

    def new_clients(self):
        """
        Function determine how many clients will arrive in specific hour
        :return: True if it's a full hour, if not - False
        """
        if self.open_hours in [60, 120, 180, 240, 300, 360]:
            number = random.randint(8, 15)
            self.clients = number
            return True
        return False

    def every_minute_tick(self):
        self.open_hours -= 1

    def next_to_the_counter(self, new_client):
        """
        next customer is served
        """
        self.current_client = new_client


class Client:
    def __init__(self, spent_time):
        """
        :param spent_time: Time that single client will be served
        """
        self.time_remain = spent_time

    def waiting(self):
        self.time_remain -= 1

    def has_been_served(self):
        """
        Function determine whether client can leave the queue
        :return:
        """
        if self.time_remain == 0:
            return True
        return False


def single_simulation(restrict, fsp):
    """
    :return: amount of people outside
    """
    bistro = Bistro(restrict, fsp)
    queue = QueueBaE()

    next_client = None
    clients_outside = 0
    client_time_range = [4, 5, 6, 7]
    client_time = random.choice(client_time_range)

    if not bistro.faster_service_pace:
        client_time += random.randint(1, 2)  # slower cashier makes service time longer

    while bistro.open_hours > 0:

        if bistro.new_clients():

            for it in range(bistro.clients):
                client = Client(client_time)
                queue.enqueue(client)

        if queue.isEmpty():  # nobody in queue, time keep going
            bistro.every_minute_tick()
            continue

        if bistro.current_client is None or next_client.has_been_served():
            next_client = queue.dequeue()
            bistro.next_to_the_counter(next_client)

        if queue.size() >= bistro.restricted_amount_of_clients:
            bistro.full_queue_inside = True
        else:
            bistro.full_queue_inside = False

        next_client.waiting()
        bistro.every_minute_tick()

    if bistro.full_queue_inside:
        clients_outside = queue.size() - restrict

    return clients_outside


def interpret(restrict, n):
    """
    In this function I am going to interpret _1 as calculations for faster cashier, similary _2 for the slower one
    """
    list_of_clients_outside_1, list_of_clients_outside_2, x = [], [], []
    average_amount_1, average_amount_2 = 0, 0

    for i in range(n):
        data_1 = single_simulation(restrict, True)
        list_of_clients_outside_1.append(data_1)
        data_2 = single_simulation(restrict, False)
        list_of_clients_outside_2.append(data_2)

        x.append(i)

    for num in list_of_clients_outside_1:
        average_amount_1 += num

    for num in list_of_clients_outside_2:
        average_amount_2 += num

    result_1, result_2 = average_amount_1 / len(list_of_clients_outside_1), average_amount_2 / len(list_of_clients_outside_2)

    values_1 = list_of_clients_outside_1
    values_2 = list_of_clients_outside_2
    plt.scatter(x, values_1, c="blue", label="Faster")
    plt.scatter(x, values_2, c="red", label="Slower")

    plt.plot(x, [result_1 for i in range(n)], label="average Faster")
    plt.plot(x, [result_2 for i in range(n)], label="average Slower")

    plt.title("Simulation")
    plt.xlabel("Single days")
    plt.ylabel("Customers outside")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == '__main__':
    interpret(6, 25)
    interpret(10, 20)
    interpret(23, 20)
