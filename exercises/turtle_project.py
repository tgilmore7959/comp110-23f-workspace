"""Beach scene."""
 
__author__ = "730585444"
 
from turtle import Turtle, done 
turt = Turtle()


def draw_water(turt: Turtle) -> None:
    """Draws water."""
    turt.penup()
    turt.color("blue")
    turt.width(5)
    y = -200
    while y < 0: 
        turt.goto(-250, y)
        turt.pendown()
        
        x = -250
        while x < 250:  
            turt.goto(x, y)
            turt.goto(x + 20, y + 20)
            turt.goto(x + 40, y)
            x += 40
        
        y += 40
        turt.penup()
     

def draw_sand(turt: Turtle) -> None:
    """Draws the sand."""
    turt.penup()
    turt.goto(-250, -200)
    turt.color("goldenrod")
    turt.begin_fill()
    turt.goto(250, -200)
    turt.goto(250, -300)
    turt.goto(-250, -300)
    turt.goto(-250, -200)
    turt.end_fill()

 
def draw_sun(turt: Turtle, x: float, y: float) -> None:
    """Draws the Sun."""
    turt.penup()
    turt.goto(x, y)
    turt.color("yellow")
    turt.begin_fill()
    turt.circle(50)
    turt.end_fill()


def draw_tree(turt: Turtle, x: float, y: float) -> None:
    """Draws a tree at coord."""
    # Trunks
    turt.penup()
    turt.goto(x, y)
    turt.color("brown")
    turt.begin_fill()
    turt.pendown()
    # Width
    turt.forward(30)
    turt.left(90)
    # Height
    turt.forward(100)
    turt.left(90)
    turt.forward(30)
    turt.left(90)
    turt.forward(100)
    turt.left(90)
    turt.end_fill()
    turt.penup()
    # Move up to leaves
    turt.goto(x - 15, y + 100)  # Adjusted start position for the foliage
    turt.color("green")
    turt.begin_fill()
    turt.pendown()
    for _ in range(4):  # Draw square
        turt.forward(60)  # Foliage width
        turt.left(90)
    turt.end_fill()


def main() -> None:
    """Runs all drawing."""
    draw_sun(turt, -210, 150)
    draw_water(turt)
    draw_sand(turt)
    draw_tree(turt, -200, -250)
    draw_tree(turt, 200, -250)


if __name__ == "__main__":
    main()


done()