from turtle import*
import time
def main():
    speed(10)
    bgcolor('pink')
    penup()
    goto(0, -100)
    pendown()
    pensize(5)
    pencolor('black')
    circle(130)
    penup()

    #right eye
    goto(50,60)
    pendown()
    pencolor('green')
    begin_fill()
    circle(30)
    end_fill()
    penup()

    #left eye
    goto(-50,60)
    pendown()
    pencolor('brown')
    begin_fill()
    circle(30)
    end_fill()
    penup()

    #nose
    penup()
    goto(0,10)
    pensize(20)
    pendown()
    forward(125)
    left(90)
    penup()
    
   
#The mouth
    goto(-40,-20)
    pensize(2)
    pendown()
    right(100)
    right(20)
    right(90)
    goto(40,-20)
    goto(0,-60)
    goto(-40,-20)



    

main()





















