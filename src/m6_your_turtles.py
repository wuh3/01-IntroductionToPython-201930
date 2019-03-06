"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Haozhe Wu.
"""
########################################################################
# done
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# done
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window=rg.TurtleWindow
dakota=rg.SimpleTurtle()
dakota.pen=rg.Pen('purple',3)
dakota.speed=100
size=50
for k in range (49):
    dakota.draw_circle(size)
    dakota.forward(100)
    dakota.left(50)
    dakota.pen_up()
    dakota.backward(20)
    dakota.pen_down()
indiana=rg.SimpleTurtle()
indiana.backward(200)
indiana.pen=rg.Pen('blue',3)

indiana.speed=200
size1=5
for k in range(30):
    indiana.draw_regular_polygon(5,size1)
    indiana.forward(10)
    indiana.right(10)
    indiana.left(20)
    size1=size1+1
