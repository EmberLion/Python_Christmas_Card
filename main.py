import pygame
import turtle
from random import randint

# set background
bg = turtle.Screen()
bg.bgpic("winterscene4.gif")

# play music
pygame.mixer.init()
pygame.mixer.music.load("wewishyouamerryc.wav")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)

# hide turtle
turtle.hideturtle()

# writing message
turtle.penup()
turtle.goto(-300, 250)
# You can edit the card here!
turtle.write('Merry Christmas, God bless you!', font = ['Arial', 30, 'normal'])

while True:
    # defining koch snowflake function
    def draw_koch(t, iterations, length, short_factor, angle):
        if iterations == 0:
            t.forward(length)
        else:
            iterations = iterations - 1
            length = length / short_factor
            draw_koch(t, iterations, length, short_factor, angle)
            t.left(angle)
            draw_koch(t, iterations, length, short_factor, angle)
            t.right(angle * 2)
            draw_koch(t, iterations, length, short_factor, angle)
            t.left(angle)
            draw_koch(t, iterations, length, short_factor, angle)


    # defining turtle and hiding it
    t = turtle.Turtle()

    # turning up the speed :)
    t.speed(10000000000000)

    # using the draw_koch() function
    for i in range(3):
        draw_koch(t, 4, 100, 3, 60)
        t.right(120)

    while True:
       # making the turtle start in a random position
       t.penup()
       t.goto(randint(-500, 0), randint(0, 100))
       t.pendown()
       t.fillcolor('blue')
       t.begin_fill()
       for i in range(3):
            draw_koch(t, 4, 100, 3, 60)
            t.right(120)


    turtle.mainloop()




