import matplotlib.pyplot as plt
import random
import numpy as np
import os
import imageio
import natsort
import argparse
import sys


def generate_moves(n, size, anim_path):
    """
    Function simulates the movements of the agent on the grid and saves each move as a png file
    :param n: the number of moves that the agent is to do
    :param size: distance from the point (0, 0) on each side
    :param anim_path: path to the folder where photos and gifs are to be saved
    """
    os.chdir(anim_path)

    start_position = [0, 0]
    x_moves, y_moves = [0], [0]
    x, y = start_position[0], start_position[1]
    for i in range(n):
        if random.choice([0, 1]) == int(1):
            if x == size:
                x -= 1
            elif x == -size:
                x += 1
            else:
                x += random.choice([-1, 1])
        else:
            if y == size:
                y -= 1
            elif y == -size:
                y += 1
            else:
                y += random.choice([-1, 1])
        x_moves.append(x)
        y_moves.append(y)
        plt.plot(x_moves[-2:], y_moves[-2:], 'o-m', alpha=0.2)
        plt.savefig(str(i + 1))


def save_moves(n, size: int, anim_path):
    """
    An additional function that regulates the settings of the graph and the grid
    :param n: the number of moves that the agent is to do
    :param size: distance from the point (0, 0) on each side
    :param anim_path: path to the folder where photos and gifs are to be saved
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    plt.xlim([-size, size])
    plt.ylim([-size, size])
    ax.xaxis.set_ticks(np.arange(-size, size + 1, 1))
    ax.yaxis.set_ticks(np.arange(-size, size + 1, 1))
    ax.xaxis.set_ticklabels([])
    ax.yaxis.set_ticklabels([])
    plt.grid(alpha=0.33)
    plt.title("super random moves of the super agent")
    generate_moves(n, size, anim_path)


def animation(n, size, anim_path):
    """
    Function that creates a gif from previously generated agent movements
    :param n: the number of moves that the agent is to do
    :param size: distance from the point (0, 0) on each side
    :param anim_path: path to the folder where photos and gifs are to be saved
    """
    save_moves(n, size, anim_path)

    gif_number = 0
    specific_number = 0
    while gif_number >= 0:
        name = "gif-{}.gif".format(gif_number)
        try_gif_path = os.path.join(anim_path, name)
        if os.path.exists(try_gif_path):
            gif_number += 1
        else:
            specific_number = gif_number
            gif_number = -1

    name_gif = "gif-{}.gif".format(specific_number)
    gif_path = os.path.join(anim_path, name_gif)

    writer = imageio.get_writer(gif_path, fps=2)
    files_list = natsort.natsorted(os.listdir(anim_path))
    for file_name in files_list:
        if file_name.endswith(".png"):
            file_path = os.path.join(anim_path, file_name)
            image = imageio.imread(file_path)
            writer.append_data(image)


def simulate_agent_moves(n, size, anim_path):
    """
    The final function which checks if the selected folder for saving the animation is empty
     and deletes previous simulation executions
    :param n: the number of moves that the agent is to do
    :param size: distance from the point (0, 0) on each side
    :param anim_path: path to the folder where photos and gifs are to be saved
    """
    if n > 0 and size > 0:
        if os.path.exists(anim_path) and os.path.isdir(anim_path):

            if len(os.listdir(anim_path)) == 0:
                animation(n, size, anim_path)
            else:
                for file in os.listdir(anim_path):
                    if file.endswith(".png"):
                        os.remove(os.path.join(anim_path, file))
                    else:
                        pass
                animation(n, size, anim_path)
        else:
            raise FileExistsError("Wrong path")
    else:
        raise ValueError("n and size must be greater than 0")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Function simulates the movements of the agent on the grid and makes a gif of every move. "
              "Type --help to check the needed arguments.")
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument("-n", type=int, help="the number of moves that the agent is to do")
        parser.add_argument("-s", "--size", type=int, help="distance from the point (0, 0) on each side")
        parser.add_argument("-p", "--anim_path", type=str, help="path to the folder where photos and gifs"
                                                                " are to be saved")
        args = parser.parse_args()

        simulate_agent_moves(args.n, args.size, args.anim_path)
