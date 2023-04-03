from L7_ZAD1_5 import *


def water_transfer(f_bucket, s_bucket, cap):
    if cap > f_bucket and cap > s_bucket:
        raise ValueError("Expected volume is too large")

    if f_bucket == s_bucket:
        if cap == f_bucket:
            raise ValueError("You already have this volume")
        else:
            raise ValueError("Containers are the same size")

    g = Graph()
    for f in range(f_bucket + 1):
        for s in range(s_bucket + 1):
            frc = f_bucket - f  # rc - ramaining capacity
            src = s_bucket - s
            stage = (f, s)
            g.add_edge(stage, (f_bucket, s))
            g.add_edge(stage, (f, s_bucket))
            g.add_edge(stage, (f, 0))
            g.add_edge(stage, (0, s))
            if f > src:
                g.add_edge(stage, (f - src, s + src))
            else:
                g.add_edge(stage, (0, s + f))
            if s > frc:
                g.add_edge(stage, (f + frc, s - frc))
            else:
                g.add_edge(stage, (s + f, 0))

    if f_bucket > cap and s_bucket > cap:
        route = min([g.get_route_only((0, 0), (cap, 0)), g.get_route_only((0, 0), (0, cap))], key=len)
    else:
        if f_bucket > cap:
            route = g.get_route_only((0, 0), (cap, 0))
        else:
            route = g.get_route_only((0, 0), (0, cap))
    final_ret = ""
    for val in route:
        final_ret += " -> {}".format(val)
    return final_ret
