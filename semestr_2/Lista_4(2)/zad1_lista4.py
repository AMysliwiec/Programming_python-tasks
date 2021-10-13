import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import argparse
from fractions import Fraction
import sys


def f(u, T, Q, w, A):
    """
    function solves the equation of motion of a mathematical pendulum
    :param u:
    :param T: pendulum time of motion
    :param Q: forcing force
    :param w: angular velocity
    :param A: amplitude(?)
    :return: equation
    """
    theta, omega = u[0], u[1]
    return [omega, -(1/Q) * omega - np.sin(theta) + A * np.cos(w * T)]


def figure(th0, v0, Q, w, A):
    """
    visualization of the motion of the pendulum
    :param v0: initial velocity
    :param th0: initial angle
    :param Q: forcing force
    :param w: angular velocity
    :param A: amplitude(?)
    """
    u0 = [th0, v0]
    T = np.linspace(0, 50, 300)
    us = odeint(f, u0, T, args=(Q, w, A))
    ys = us[:, 0]
    vs = us[:, 1]
    plt.xlabel("t")
    plt.legend(["theta(t)", "v(t)"], loc="upper right")
    plt.grid(alpha=0.5)
    plt.title("Mathematics pendulum")
    plt.plot(T, ys, "c")
    plt.plot(T, vs, "m")
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Function solves the equation of motion of a mathematical pendulum and visualizes it."
              " Type --help for the list of needed variables")
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument("-Q", type=float, help="forcing force")
        parser.add_argument("-w", type=Fraction, help="angular velocity")
        parser.add_argument("-A", type=float, help="amplitude(?)")
        parser.add_argument("-th0", type=float, help="initial angle")
        parser.add_argument("-v0", type=float, help="initial velocity")
        args = parser.parse_args()

        figure(args.th0, args.v0, args.Q, args.w, args.A)

