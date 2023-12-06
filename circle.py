import turtle
import colorsys

# Set up the turtle
turtle.speed(0)
turtle.bgcolor("black")
turtle.hideturtle()

# Function to draw a colorful circular pattern
def draw_circles(num_circles, radius):
    for _ in range(num_circles):
        hue = (turtle.heading() / 360.0) % 1.0
        color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        turtle.color(color)
        turtle.circle(radius)
        turtle.left(360 / num_circles)

# Draw the colorful circular pattern
draw_circles(36, 50)  # 36 circles with radius 50

# Close the window on click
turtle.exitonclick()
