import turtle

# create a turtle object
heart = turtle.Turtle()

# set the fill color to red
heart.fillcolor('red')
heart.begin_fill()

# Draw the heart shape
heart.left(45)
heart.forward(100)
heart.circle(50, 180)
heart.right(90)
heart.circle(50, 180)
heart.forward(100)

# end the fill
heart.end_fill()
heart.hideturtle()

# keep the turtle graphics windows open until it is closed
turtle.done()