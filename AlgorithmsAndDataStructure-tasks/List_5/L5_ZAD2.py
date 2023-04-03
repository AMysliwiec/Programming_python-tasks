class Tower:
    """
    A stack for the construction of rods for the tower of hanoi problem
    """
    def __init__(self, name):
        self.disks = []
        self.name = name

    def isEmpty(self):
        return self.disks == []

    def push(self, item):
        self.disks.append(item)

    def pop(self):
        return self.disks.pop()

    def peek(self):
        return self.disks[len(self.disks) - 1]

    def size(self):
        return len(self.disks)

    def get_name(self):
        return self.name

    def __getitem__(self, item):
        return self.disks[item]

    def __str__(self):
        return str(self.disks)


def move(a, b):
    """
    The function shows the current path traveled by the disk
    :param a: from which rod
    :param b: to which rod
    """
    print("moving disk from {} to {}".format(a, b))


def disk_movement(source, helper, target, height):
    if height <= 0:
        raise ValueError("At least one disk is needed to build the tower")
    elif height == 1:
        target.push(source.pop())
        move(source.get_name(), target.get_name())
        return target
    else:
        disk_movement(source, target, helper, height - 1)
        target.push(source.pop())
        move(source.get_name(), target.get_name())
        disk_movement(helper, source, target, height - 1)
        return target


def Hanoi(height):
    A = Tower("A")
    B = Tower("B")
    C = Tower("C")
    for disk in range(1, height + 1):
        A.push(disk)
    return disk_movement(A, B, C, height)

