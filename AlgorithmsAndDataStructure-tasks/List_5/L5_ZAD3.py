import turtle


def turtle_moves(level, angle, step):
    """
    function defines the movement of the turtle
    :param level: level of recursion
    :param angle: rotation angle (90)
    :param step: length of the "step" of the turtle
    :return:
    """
    if level == 0:
        return

    turtle.left(angle)
    turtle_moves(level - 1, -angle, step)

    turtle.forward(step)
    turtle.right(angle)
    turtle_moves(level - 1, angle, step)

    turtle.forward(step)
    turtle_moves(level - 1, angle, step)

    turtle.right(angle)
    turtle.forward(step)
    turtle_moves(level - 1, -angle, step)

    turtle.left(angle)


def hilbert_curve(level):
    """
    main function of drawing a curve
    """
    turtle.speed(0)
    turtle.width(2)

    window = turtle.Screen()
    # window.bgpic('mario.gif')
    window.bgcolor('lightgreen')
    window.title("Hilbert curve")
    size = 300                              # for mario.gif it was 200, because the curve covered the ground :)
    turtle.color('green')
    turtle.penup()
    turtle.goto(-size / 2.0, -size / 2.0)   # to center the curve
    turtle.pendown()

    step_length = (2 ** level - 1 / (2 ** level))
    turtle_moves(level, angle=90, step=size / step_length)
    turtle.mainloop()
