"""
This module contains program code which creates a GUI for plotting function
"""

from PyQt5.QtWidgets import QApplication, QCheckBox, QMessageBox, QMainWindow, QWidget, QGridLayout, QLineEdit, QLabel
from PyQt5.QtWidgets import QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as canvas
from functools import partial
import qtmodern.styles
import qtmodern.windows
import numpy as np
import random
import sys


class DisplayMaker(QMainWindow):
    """
    Class responsible for creating the entire interface
    """

    def __init__(self):
        """
        Constructor that contains the window title, size and initializes the function responsible
        for the interface appearance
        """
        super().__init__()

        self.setWindowTitle("Superb plotting")
        self.setFixedSize(800, 900)

        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.main_widget.setLayout(self.main_layout)

        self.create_window()
        self.example()

    def create_window(self):
        """
        Function makes 3 main layouts. First at the top it creates a place to enter the function formulas, sizes of both
        x and y axes, the title of the graph and axis, functional buttons and legend checkbox.
        Then there is a button layout that makes it easier to build functions and at the bottom there is a place
        to display the finished graph.
        """

        self.label_info = QLabel()
        self.label_info.setText("Type function formula, you can also add some more by adding ';'")
        self.label_info.setFixedHeight(40)

        self.main_layout.addWidget(self.label_info)

        self.entry = QLineEdit()
        self.entry.setFixedHeight(40)
        self.entry.setAlignment(Qt.AlignLeft)
        self.entry.setReadOnly(False)

        self.main_layout.addWidget(self.entry)

        self.buttons = {}
        to_entry_layout = QGridLayout()

        self.entry_x = QLineEdit()
        self.entry_x.setFixedWidth(70)
        self.x_lim_label = QLabel()
        self.x_lim_label.setText("x axis range: ")

        self.x_title = QLineEdit()
        self.x_label = QLabel()
        self.x_label.setText("x label title: ")

        self.entry_y = QLineEdit()
        self.entry_y.setFixedWidth(70)
        self.y_lim_label = QLabel()
        self.y_lim_label.setText("y axis range: ")

        self.y_title = QLineEdit()
        self.y_label = QLabel()
        self.y_label.setText("y label title: ")

        self.figure_title = QLineEdit()
        self.title_label = QLabel()
        self.title_label.setText("Title:")

        widgets = [self.x_lim_label, self.entry_x, self.x_label, self.x_title, self.title_label, self.y_lim_label,
                   self.entry_y, self.y_label, self.y_title, self.figure_title]
        pos = [(i, j) for i in range(0, 2) for j in range(1, 6)]

        for i in widgets:
            to_entry_layout.addWidget(i, pos[widgets.index(i)][0], pos[widgets.index(i)][1])

        self.legend = QCheckBox("Legend")
        self.legend.setChecked(True)

        to_entry_layout.addWidget(self.legend, 0, 8)

        self.buttons[";"] = QPushButton(";")
        to_entry_layout.addWidget(self.buttons[";"], 0, 7)

        self.buttons["draw"] = QPushButton("draw")
        to_entry_layout.addWidget(self.buttons["draw"], 0, 9)

        self.buttons["set titles"] = QPushButton("set titles")
        to_entry_layout.addWidget(self.buttons["set titles"], 1, 9)

        self.buttons["set axis"] = QPushButton("set axis")
        to_entry_layout.addWidget(self.buttons["set axis"], 1, 8)

        self.buttons["clear"] = QPushButton("clear")
        # self.buttons["clear"].setStyleSheet("background-image : url(pi.jpg);")
        to_entry_layout.addWidget(self.buttons["clear"], 1, 7)

        buttons_layout = QGridLayout()
        to_push = ["(", ")", "|", "sin", "x", "+", "-", "sqrt", "cos", "pi", "*", "/", "^", "tan", "e"]
        positions = [(i, j) for i in range(4, 7) for j in range(1, 6)]

        for i in to_push:
            self.buttons[i] = QPushButton(i)
            buttons_layout.addWidget(self.buttons[i], positions[to_push.index(i)][0], positions[to_push.index(i)][1])

        self.figure = plt.figure()
        self.grid = plt.grid(True)
        self.canvas = canvas(self.figure)
        canva_layout = QVBoxLayout()
        canva_layout.addWidget(self.canvas)

        for layout in [to_entry_layout, buttons_layout, canva_layout]:
            self.main_layout.addLayout(layout)

    def example(self):
        """
        Function shows how the GUI works
        """
        self.entry.setText("x^2; e^(x)")
        self.entry_x.setText("-5, 5")
        self.entry_y.setText("-5, 5")
        self.x_title.setText("x")
        self.y_title.setText("y")
        self.figure_title.setText("Exemplary figure")

    def set_entry(self, text: str):
        """
        Function changes the entered text in entry area, in this file it is used to reset entered data
        :param text: wanted string to enter
        """
        self.entry.setText(text)
        self.entry.setFocus()

    def set_titles(self, text: str):
        """
        Function changes every entered title, in this file it is used to reset entered data
        :param text: wanted string to enter
        """
        for titles in [self.figure_title, self.y_title, self.x_title]:
            titles.setText(text)
        self.x_title.setFocus()

    def set_axis(self, text: str):
        """
        Function changes entered axis dimensions, in this file it is used to reset entered data
        :param text: wanted string to enter
        """
        for entry_place in [self.entry_x, self.entry_y]:
            entry_place.setText(text)
        self.entry_x.setFocus()


def make_it_possible(input_txt: str):
    """
    Function replaces the mathematical symbols with their equivalents that are readable by the program
    :param input_txt: string to be checked
    :return: a finished string with the replaced symbols
    """

    for symbol in ["sin", "cos", "tan", "sqrt", "e", "pi"]:
        if symbol in input_txt:
            input_txt = input_txt.replace(symbol, "np.{}".format(symbol))

    if "|" in input_txt:
        amount = int(input_txt.count("|"))
        for i in range(int(amount / 2)):
            input_txt = input_txt.replace("|", "abs(", 1)
            input_txt = input_txt.replace("|", ")", 1)

    if "^" in input_txt:
        input_txt = input_txt.replace("^", "**")

    if ")(" in input_txt:
        input_txt = input_txt.replace(")(", ")*(")

    if "np.e^" in input_txt:
        input_txt = input_txt.replace("np.e^", "np.exp")

    el = ["{}x".format(i) for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "pi", ")", "x", "e"]]
    for i in el:
        if i in input_txt:
            input_txt = input_txt.replace(i, "{}*{}".format(i[0], i[-1]))

    if "e*xp" in input_txt:
        input_txt = input_txt.replace("e*xp", "exp")

    return input_txt.strip()


class FigureMaker:
    """
    Class that combines functionality and creates an output for the DisplayMaker class
    """

    def __init__(self, window):
        """
        Constructor that contains the interface and initialize the function that gives the utility to buttons
        :param window: window created by DisplayMaker
        """
        self.window = window

        self.connect_buttons()
        self.message = QMessageBox()

    def add_element(self, to_add):
        """
        Function by which pressing the button adds an element to the existing function formula
        :param to_add: the text displayed by pushing a specific button
        """
        element = self.window.entry.text() + to_add
        self.window.set_entry(element)

    def connect_buttons(self):
        """
        Functions gives utility to the function buttons
        """
        for btn_output, btn in self.window.buttons.items():
            if btn_output not in {"draw", "clear", "set axis", "set titles"}:
                btn.clicked.connect(partial(self.add_element, btn_output))

        self.window.buttons["draw"].clicked.connect(self.drawing)
        self.window.buttons["clear"].clicked.connect(partial(self.window.set_entry, ""))
        self.window.buttons["set axis"].clicked.connect(partial(self.window.set_axis, ""))
        self.window.buttons["set titles"].clicked.connect(partial(self.window.set_titles, ""))

    def get_functions(self):
        """
        Function takes the entered formula string and returns a list of single ones
        :return: list of separate function formulas
        """
        return self.window.entry.text().split(";")

    def drawing(self):
        """
        Function uses the entire entered data to create a graph
        """

        list_of_function = self.get_functions()
        x_axis = self.window.entry_x.text().split(",")
        y_axis = self.window.entry_y.text().split(",")
        if len(x_axis) != 2 or len(y_axis) != 2:
            self.message.critical(self.window, "Error",
                                  "Enter the minimum and maximum value on the axis separated by ','")
            return

        x_min, x_max = x_axis[0], x_axis[1]
        y_min, y_max = y_axis[0], y_axis[1]

        try:
            x_min = int(x_min)
            x_max = int(x_max)
            y_min = int(y_min)
            y_max = int(y_max)
        except ValueError:
            self.message.critical(self.window, "Error", "Values on the axes must be numbers")
            return

        if x_min >= x_max:
            self.message.critical(self.window, "Error", "Minimal x cannot be bigger than the maximal x")
            return

        if y_min >= y_max:
            self.message.critcal(self.window, "Error", "Minimal y cannot be bigger than the maximal y")
            return

        if "sqrt" in self.window.entry.text() or "np.log" in self.window.entry.text():
            if x_max < 0:
                self.message.critical(self.window, "Error", "This function does not take negative values")
                return
            elif x_min < 0:
                x_min = 0
                self.message.about(self.window, "Info", "Drawing function from 0 to {}".format(x_max))

        x = np.arange(x_min, x_max, 0.1)

        title = self.window.figure_title.text()
        x_label = self.window.x_title.text()
        y_label = self.window.y_title.text()

        self.window.figure.clear()
        ax = self.window.figure.add_subplot()

        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.xlim(x_min, x_max)
        plt.ylim(y_min, y_max)
        plt.grid(True)

        colors = ["#ff99ff", "#00CCCC", "#660066", "#808000", "#00FF00", "#FFA500", "#D2691E"]

        for formula in list_of_function:
            if "/0" in formula:
                self.message.critical(self.window, "Error",
                                      "How dare you")
                return

            formula = make_it_possible(formula)
            try:
                f = eval(formula)

                if "," in formula:
                    self.message.critical(self.window, "Error",
                                          "Bad formula, check if a ',' was entered instead of ';' or '.'")
                    return

            except SyntaxError:
                self.message.critical(self.window, "Error", "Bad formula, check if all symbols are correctly entered "
                                                            "and if ';' is in undesirable place")
                return

            except TypeError:
                self.message.critical(self.window, "Error",
                                      "Bad formula, check if any unacceptable data type is entered")
                return

            except NameError:
                self.message.critical(self.window, "Error",
                                      "Bad formula, probably some unwanted variable got into this formula")
                return

            except ZeroDivisionError:
                self.message.critical(self.window, "Error", "Pamiętaj **** nie dzieli się przez 0")
                return

            try:
                ax.plot(x, f)
            except ValueError:
                line_color = random.choice(colors)
                try:
                    if type(f) is int or type(f) is float:
                        plt.axhline(f, c=line_color)
                    else:
                        self.message.critical(self.window, "Error", "Bad formula, constant function must be a number")
                        return
                except ValueError:
                    self.message.critical(self.window, "Error", "Bad formula")
                    return

        if self.window.legend.isChecked():
            plt.legend(list_of_function)

        self.window.canvas.draw()


def main():
    """
    Function connects the entire code to be run
    """
    ap = QApplication(sys.argv)
    window = DisplayMaker()
    figure = FigureMaker(window=window)
    qtmodern.styles.dark(ap)
    mw = qtmodern.windows.ModernWindow(window)
    mw.show()
    figure.message.about(window, "Info", "Click 'draw' to see how the function works")
    sys.exit(ap.exec_())


if __name__ == "__main__":
    main()
