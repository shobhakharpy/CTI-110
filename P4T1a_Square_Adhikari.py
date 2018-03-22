# CTI 110
# Shobhakhar Adhikari
# P4T1a: Shapes

import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
sunder = turtle.Turtle()    # Create a turtle, assign to sunder

# add some display options

sunder.pensize(3)
sunder.pencolor("red")
sunder.shape("turtle")

#commands from here to the last line can be replaced 

sunder.forward(200)          # Tell sunder to move forward by 50 units
sunder.left(90)             # Tell sunder to turn by 90 degrees
sunder.forward(200)          # Complete the second side of a rectangle
sunder.left(90)
sunder.forward(200)
sunder.left(90)
sunder.forward(200)

# end commands
wn.mainloop()             # Wait for user to close window
