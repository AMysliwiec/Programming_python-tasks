import sys
from pythonds.graphs import PriorityQueue
from operator import itemgetter


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Vertex:
    def __init__(self, num):
        self.id = num
        self.connected_to = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def set_color(self, color):
        self.color = color

    def set_distance(self, d):
        self.dist = d

    def set_pred(self, p):
        self.pred = p

    def set_discovery(self, dtime):
        self.disc = dtime

    def set_finish(self, ftime):
        self.fin = ftime

    def get_finish(self):
        return self.fin

    def get_discovery(self):
        return self.disc

    def get_pred(self):
        return self.pred

    def get_distance(self):
        return self.dist

    def get_color(self):
        return self.color

    def get_connections(self):
        return self.connected_to.keys()

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    def __str__(self):
        return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(
            self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred) + "]\n"

    def get_id(self):
        return self.id


class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0
        self.steps = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def delete_vertex(self, key):
        if key in self.get_vertices_list():
            self.num_vertices -= 1
            del self.vert_list[key]

    def get_vertex(self, n):
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vert_list

    def add_edge(self, f, t, cost=0):
        if f not in self.vert_list:
            nv = self.add_vertex(f)
        if t not in self.vert_list:
            nv = self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], cost)

    def get_vertices(self):
        return self.vert_list.keys()

    def get_vertices_list(self):
        return list(self.get_vertices())

    def __iter__(self):
        return iter(self.vert_list.values())

    def dot_repr(self):
        dot_string = "digraph G {\n"
        for v in self:
            for w in v.get_connections():
                weight = v.connected_to[w]
                if weight != 0:
                    if isinstance(w.get_id(), (int, float)):
                        dot_string += '\t{} -> {} [ label = "{}" ];\n'.format(v.get_id(), w.get_id(), weight)
                    else:
                        dot_string += '\t"{}" -> "{}" [ label = "{}" ];\n'.format(v.get_id(), w.get_id(), weight)
                else:
                    if isinstance(w.get_id(), (int, float)):
                        dot_string += "\t{} -> {}\n".format(v.get_id(), w.get_id())
                    else:
                        dot_string += '\t"{}" -> "{}"\n'.format(v.get_id(), w.get_id())
        dot_string += "}"
        return dot_string

    def __str__(self):
        file = open("dot_repr.txt", 'w')
        file.writelines(self.dot_repr())
        file.close()
        return self.dot_repr()

    def bfs(self, start):
        start.set_distance(0)
        start.set_pred(None)
        vert_queue = Queue()
        vert_queue.enqueue(start)
        while vert_queue.size() > 0:
            current_vert = vert_queue.dequeue()
            for nbr in current_vert.get_connections():
                if nbr.get_color() == 'white':
                    nbr.set_color('gray')
                    nbr.set_distance(current_vert.get_distance() + 1)
                    nbr.set_pred(current_vert)
                    vert_queue.enqueue(nbr)
            current_vert.set_color('black')

    def dfs(self):
        for a_vert in self:
            a_vert.set_color('white')
            a_vert.set_pred(-1)
        for a_vert in self:
            if a_vert.get_color() == 'white':
                self.dfsvisit(a_vert)

    def dfsvisit(self, start_vert):
        start_vert.set_color('gray')
        self.steps += 1
        start_vert.set_discovery(self.steps)
        for next_vert in start_vert.get_connections():
            if next_vert.get_color() == 'white':
                next_vert.set_pred(start_vert)
                self.dfsvisit(next_vert)
        start_vert.set_color('black')
        self.steps += 1
        start_vert.set_finish(self.steps)

    def topological_sorting(self):
        self.dfs()
        verts = []
        for i in self.vert_list.keys():
            end_of_process_time = self.vert_list[i].get_finish()
            verts.append((i, end_of_process_time))
        verts.sort(key=itemgetter(1))
        sort = [i[0] for i in verts]
        sort.reverse()

        for i in range(1, self.num_vertices):
            current = sort[i]
            connections = [vert.id for vert in self.vert_list[current].get_connections()]
            for j in sort[:i]:
                if j in connections:
                    raise ValueError('Cannot sort the graph this way')
        return sort

    def dijkstra(self, start):
        pq = PriorityQueue()
        start.set_distance(0)
        pq.buildHeap([(v.get_distance(), v) for v in self])
        while not pq.isEmpty():
            current_vert = pq.delMin()
            for next_vert in current_vert.get_connections():
                new_dist = current_vert.get_distance() + current_vert.get_weight(next_vert)
                if new_dist < next_vert.get_distance():
                    next_vert.set_distance(new_dist)
                    next_vert.set_pred(current_vert)
                    pq.decreaseKey(next_vert, new_dist)

    def traverse(self, vert):
        result = []
        x = vert
        while x.get_pred():
            result.append(x.get_id())
            x = x.get_pred()
        result.append(x.get_id())
        result.reverse()
        return tuple(result)

    def fastest_route(self, start, end=None):
        self.dijkstra(self.get_vertex(start))
        routes = {}
        for vert in self.get_vertices_list():
            if vert == start:
                routes[vert] = tuple([0])
            else:
                route = self.traverse(self.get_vertex(vert))
                if start in route:
                    routes[vert] = route
                else:
                    routes[vert] = None

        for vert in self:
            vert.set_distance(sys.maxsize)

        if end is not None:
            if end in routes.keys():
                return "{}: {}".format(end, routes[end])
            else:
                raise KeyError("No such value in the graph")
        return routes

    def route_length(self, start, end=None):
        data = self.fastest_route(start, end)
        length_dict = {}
        for key in self.get_vertices_list():
            length_dict[key] = len(data[key]) - 1
        return length_dict

    def get_route_only(self, start, end):
        self.dijkstra(self.get_vertex(start))
        for vert in self.get_vertices_list():
            if vert == end:
                route = self.traverse(self.get_vertex(vert))
                return route
        raise KeyError("Cannot find the wanted key")
