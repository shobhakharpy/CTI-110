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

    
sunder.backward(100)          # Tell sunder to move forward by 50 units
sunder.right(90)                # Tell sunder to turn by 90 degrees
sunder.forward(30)
sunder.left(90)
sunder.forward(100)
sunder.right(90)
sunder.forward(30)
sunder.left(90)
sunder.backward(100)

sunder.penup()
sunder.forward(300)
sunder.pendown()
# add some display options

sunder.pensize(3)
sunder.pencolor("blue")
sunder.shape("turtle")

#commands from here to the last line can be replaced

sunder.right(60)
sunder.backward (100)
sunder.left(300)
sunder.forward(100)
sunder.backward(45)
sunder.left(120)
sunder.forward(55)
  

    
# end commands
wn.mainloop()             # Wait for user to close window

