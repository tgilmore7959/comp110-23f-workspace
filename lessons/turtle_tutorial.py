from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
leo.speed(50)
leo.pencolor("blue")
leo.fillcolor("pink")
leo.penup()
leo.goto(45, 60)
leo.pendown()
leo.begin_fill()
i: int = 0
while i<3:
   leo.forward(400)
   leo.left(120)
   i = i + 1 
leo.end_fill()

bob: Turtle = Turtle ()
bob.pencolor("darkblue")
bob.fillcolor("purple")
bob.speed(99)
bob.penup()
bob.goto(45, 60)
bob.pendown()
side_length: int = 400
i: int = 0
while (i < 900):
   bob.forward(side_length)
   bob.left(120)
   side_length = side_length * 0.99
   i = i + 1


done()

