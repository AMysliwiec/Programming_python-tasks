import turtle
import math


def turtle_moves(level, angle, step):
    """
    function defines the movement of the turtle
    :param level: level of recursion
    :param angle: rotation angle (60)
    :param step: length of the "step" of the turtle
    :return:
    """

    if level == 0:
        turtle.forward(step)
        return

    turtle_moves(level - 1, angle, step)

    turtle.left(angle)
    turtle_moves(level - 1, angle, step)

    turtle.right(180 - angle)
    turtle_moves(level - 1, angle, step)

    turtle.left(angle)
    turtle_moves(level - 1, angle, step)


def koch_curve(level, snowflake=False):
    """
    main function of drawing a curve
    :param snowflake: if True: Function draws a whole snowflake, not only a curve
    """
    turtle.speed(0)
    turtle.width(3)

    window = turtle.Screen()
    window.bgpic('ssnowy.gif')
    # window.bgcolor('midnightblue')
    window.title("Koch curve")
    size = 300
    turtle.color('white')

    step_length = 3 ** level

    if snowflake:
        turtle.penup()
        turtle.goto(-size / 2, size * math.sqrt(3) / 6)  # to center (1/6 of the height of the equilateral triangle)
        turtle.pendown()

        for _ in range(3):
            turtle_moves(level, angle=60, step=size / step_length)
            turtle.right(120)
    else:
        turtle.penup()
        turtle.backward(size / 2)  # to center the curve
        turtle.pendown()

        turtle_moves(level, angle=60, step=size / step_length)
    turtle.mainloop()
