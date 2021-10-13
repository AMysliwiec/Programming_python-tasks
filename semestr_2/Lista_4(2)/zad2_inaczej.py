import matplotlib.pyplot as plt
import random
import numpy as np
import os
import imageio
import natsort
import argparse
import sys


def generate_moves(n, animation_path):
    """
    Function simulates the movements of the agent on the grid and saves each move as a png file
    :param n: the number of moves that the agent is to do
    :param animation_path: path to the folder where photos and gifs are to be saved
    """
    if n > 0:
        if os.path.exists(animation_path):

            os.chdir(animation_path)
            x_moves, y_moves = [0], [0]
            list_of_moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for i in range(n):
                move = random.choice(list_of_moves)
                x, y = move[0], move[1]
                x += x_moves[-1]
                y += y_moves[-1]
                x_moves.append(x)
                y_moves.append(y)
            max_x, max_y = max(x_moves), max(y_moves)
            size = max(max_x, max_y)

            fig, ax = plt.subplots(figsize=(8, 8))
            plt.xlim([-size, size])
            plt.ylim([-size, size])
            ax.xaxis.set_ticks(np.arange(-size, size + 1, 1))
            ax.yaxis.set_ticks(np.arange(-size, size + 1, 1))
            ax.xaxis.set_ticklabels([])
            ax.yaxis.set_ticklabels([])
            plt.grid(alpha=0.33)
            plt.title("super random moves of the super agent")

            for i in range(n - 1):
                plt.plot(x_moves[i:i + 2], y_moves[i:i + 2], 'o-g', alpha=0.2)
                plt.savefig(str(i + 1))
        else:
            raise FileExistsError()
    else:
        raise ValueError()


def animation(n, animation_path):
    """
    Function that creates a gif from previously generated agent movements
    :param n: the number of moves that the agent is to do
    :param animation_path: path to the folder where photos and gifs are to be saved
    """
    generate_moves(n, animation_path)

    gif_number = check_file_number(animation_path)

    name_gif = "gif-{}.gif".format(gif_number)
    gif_path = os.path.join(animation_path, name_gif)

    writer = imageio.get_writer(gif_path, fps=2)
    files_list = natsort.natsorted(os.listdir(animation_path))
    for file_name in files_list:
        if file_name.endswith(".png"):
            file_path = os.path.join(animation_path, file_name)
            image = imageio.imread(file_path)
            writer.append_data(image)


def simulate2(n, animation_path):
    """
    The final function which checks if the selected folder for saving the animation is empty
     and deletes previous simulation executions
    :param n: the number of moves that the agent is to do
    :param animation_path: path to the folder where photos and gifs are to be saved
    """
    if n > 0:
        if os.path.exists(animation_path) and os.path.isdir(animation_path):

            if len(os.listdir(animation_path)) == 0:
                animation(n, animation_path)
            else:
                for file in os.listdir(animation_path):
                    if file.endswith(".png"):
                        os.remove(os.path.join(animation_path, file))
                    else:
                        pass
                animation(n, animation_path)
        else:
            raise FileExistsError("Wrong path")
    else:
        raise ValueError("n must be greater than 0")


def check_file_number(path: str):
    """
    function checks if the gif with the given number already exists and checks which number is next
    :param path: wanted to check path
    :return: number of the next existing gif
    """
    if os.path.exists(path):
        number = 0
        specific_number = 0
        while number >= 0:
            name = "gif-{}.gif".format(number)
            try_file_path = os.path.join(path, name)
            if os.path.exists(try_file_path):
                number += 1
            else:
                specific_number = number
                number = -1
        return specific_number
    else:
        raise FileExistsError()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Function simulates the movements of the agent on the grid and makes a gif of every move. "
              "Type --help to check the needed arguments.")
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument("-n", type=int, help="the number of moves that the agent is to do")
        parser.add_argument("-p", "--animation_path", type=str, help="path to the folder where photos and gifs"
                                                                     " are to be saved")
        args = parser.parse_args()

        simulate2(args.n, args.animation_path)
