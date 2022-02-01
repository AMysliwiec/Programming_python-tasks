from L7_ZAD1_5 import *


def mis_can_problem(mis, can):
    if mis < can:
        raise ValueError("You already know the ending of this story, the preponderance of cannibals is not a good idea")

    g = Graph()
    for m in range(mis + 1):
        if m == 0:
            for c in range(can + 1):
                g.add_vertex((m, c, 0))
                g.add_vertex((m, c, 1))
        else:
            for c in range(m + 1):  # nie moze byc wiecej kanibali niż misjonarzy
                g.add_vertex((m, c, 0))
                g.add_vertex((m, c, 1))

    for vert in g.get_vertices_list():  # po drugiej stronie również
        current_mis, current_can = vert[0], vert[1]
        if current_mis not in [0, mis]:
            if current_mis >= current_can and mis - current_mis >= can - current_can:
                pass
            else:
                g.delete_vertex(vert)

    options = []
    for vert in g.get_vertices_list():
        river_bank_side = vert[2]
        current_mis, current_can = vert[0], vert[1]
        if river_bank_side == 1:   # przepłynięcie na drugą stronę
            options.append((current_mis - 1, current_can, 0))
            options.append((current_mis, current_can - 1, 0))
            options.append((current_mis - 1, current_can - 1, 0))
            options.append((current_mis - 2, current_can, 0))
            options.append((current_mis, current_can - 2, 0))
            for o in options:
                if o in g.get_vertices_list():
                    g.add_edge(vert, o)
        elif river_bank_side == 0:  # powrót
            options.append((current_mis + 1, current_can, 1))
            options.append((current_mis, current_can + 1, 1))
            options.append((current_mis + 1, current_can + 1, 1))
            options.append((current_mis + 2, current_can, 1))
            options.append((current_mis, current_can + 2, 1))
            for o in options:
                if o in g.get_vertices_list():
                    g.add_edge(vert, o)
        options = []

    route = g.get_route_only((mis, can, 1), (0, 0, 0))
    final_ret = ""
    for step in route:   # aby przejscie pokazywały stan w miejscu gdzie znajduje sie łódź
        if step[2] == 0:
            step = (mis - step[0], can - step[1], 0)
        final_ret += "-> {} ".format(step)
    return final_ret
