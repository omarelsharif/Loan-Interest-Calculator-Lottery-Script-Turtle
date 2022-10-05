#Question 6


x0 = int(input("Enter point 1's x coordinate: "))
y0 = int(input("Enter point 1's y coordinate: "))

x1 = int(input("Enter point 2's x coordinate: "))
y1 = int(input("Enter point 2's y coordinate: "))

x2 = int(input("Enter point 3's x coordinate: "))
y2 = int(input("Enter point 3's y coordinate: "))



var = (x1-x0)*(y1-y0)-(x2-x0)*(y1-y0)
p = 0

#samecheck = ((y1-y0)**2 + (x1-x0)**2  )**0.5





if var > 0:
    p = "P2 Is on the left side of the line"
    print("P2 Is on the left side of the line") 
    
if var < 0:
    p = "P2 Is on the right side of the line"
    print("P2 Is on the right side of the line") 

if var ==0:
    p = "P2 Is on the same line"
    print("P2 Is on the same line")

import turtle
turtle.home()
turtle.penup()
turtle.goto(x0,y0)
g = ("P1 " + "("+str(x0)+ ", "+str(y0)+")")
turtle.write(g, font =("Times", 7)) 



turtle.pendown()
turtle.goto(x1,y1)
g = ("P2 " + "(" +str(x1)+", "+str(y1)+")")
turtle.write(g, font =("Times", 7)) 



turtle.penup()
turtle.goto(x2,y2)




turtle.hideturtle()

turtle.dot(15)

y2 = y2-20
turtle.goto(x2,y2)

turtle.write(p, font =("Times", 7)) 




