#READ THE NOTICE ABOVE BEFORE USING THIS PARTICULAR SOFTWARE
import turtle
import random
import time
from turtle import *

window = turtle.Screen()#Creating game window
window.tracer(0)#To prevent confusing gameplay
window.title('PAC MAN FOR MACINTOSH')#For Macintosh computers(despite DVD still working on Windows computers)
window.bgcolor('black')#Black backgroung color
window.setup(600, 600)#3600000 px^2 game window

pac_s_lives = 3#Pacman has a max of 3 lives
gamescore = 0#Initial gamescore is 0

pacman = turtle.Turtle()#Defining pacman as a Turtle sprite
pacman.penup()#To prevent trace created by Pacman which causes confusing gameplay
pacman.speed(0)#Pacman is at his fastest speed
pacman.color('yellow')#Pacman is yellow
pacman.shape('circle')#Pacman is a circle
pacman.direction = 'stop'

pen = turtle.Turtle()
pen.speed(0)#Fast accurate updates in life/score happen
pen.color('blue')#life/scoreboard will be blue
pen.penup()#Avoid tracks created by scoreboard, which can produce confusing or perhaps fraudelent results
pen.goto(0, 245)#life/scoreboard will be centered around coordinate (0, 245)
pen.write('GAMESCORE:{} LIVES REMAINING:{}'.format(gamescore, pac_s_lives), align = 'center', font=('Courier',20))#Life/Scoreboard will have working scoreboard and will be center aligned at point (0, 245), have size of 36 in the "Courier" font

pac_s_foods = []#Pacman's food
for _ in range(69):#Creating 40 foodstuff items for Pacman
    pac_s_food = turtle.Turtle()#Defining pacmans food as a Turtle sprite
    pac_s_food.speed(0)#Pacman's food will be at its fastest speed(if additional code was added allowing Pacman's food to be movable)
    pac_s_food.penup()#Avoid tracks created by food, to prevent illusions, which are part of confusing gameplay.
    pac_s_food.color('orange')#Pacman's food is orange
    pac_s_food.shape('circle')#Pacman's food is in the form of a circle
    pac_s_food.shapesize(stretch_wid = 0.4, stretch_len = 0.4)#Pacman's food will have a width of 0.4 and a length of 0.4(meaning that the stretch factor of the object in respect to the x axis/variable x is 0.4, and the stretch factor of the object in respect to the  y axis/variable y is 0.4 )
    x = random.randint(-280, 280)#the x value for the food's location lies in interval -280 <= x <= 280, where x is an integer. The min x value where food can be placed is -280, and the max x value where food can be placed is 280
    y = random.randint(-280, 280)#the y value for the food's location lies in interval -280 <= y <= 280, where y is an integer. The  min y value where food can be placed is -280, and the max y value where food can be placed is 280
    pac_s_food.setposition(x, y)#Food will be placed on a random (x, y) coordinate, where -280 <= x <= 280, where x is an integer, and -280<=y<=280, where y is an integer
    pac_s_foods.append(pac_s_food)#Pacman's foodstuff items will be in the list pac_s_foods.

pac_s_foods2 = []
for _ in range(100):
    pac_s_food2 = turtle.Turtle()
    pac_s_food2.speed(0)
    pac_s_food2.penup()
    pac_s_food2.color('blue')
    pac_s_food2.shape('circle')
    pac_s_food2.shapesize(stretch_wid = 0.4, stretch_len = 0.4)
    x = random.randint(-280, 280)
    y = 280
    pac_s_food2.setposition(x, y)
    pac_s_foods2.append(pac_s_food2)

pac_s_foods3 = []
for _ in range(100):
    pac_s_food3 = turtle.Turtle()
    pac_s_food3.speed(0)
    pac_s_food3.penup()
    pac_s_food3.color('blue')
    pac_s_food3.shape('circle')
    pac_s_food3.shapesize(stretch_wid = 0.4, stretch_len = 0.4)
    x = random.randint(-280, 280)
    y = -280
    pac_s_food3.setposition(x, y)
    pac_s_foods3.append(pac_s_food3)


pac_s_foods4 = []
for _ in range(100):
    pac_s_food4 = turtle.Turtle()
    pac_s_food4.speed(0)
    pac_s_food4.penup()
    pac_s_food4.color('blue')
    pac_s_food4.shape('circle')
    pac_s_food4.shapesize(stretch_wid = 0.4, stretch_len = 0.4)
    x = 280
    y = random.randint(-280, 280)
    pac_s_food4.setposition(x, y)
    pac_s_foods4.append(pac_s_food4)

pac_s_foods5 = []
for _ in range(100):
    pac_s_food5 = turtle.Turtle()
    pac_s_food5.speed(0)
    pac_s_food5.penup()
    pac_s_food5.color('blue')
    pac_s_food5.shape('circle')
    pac_s_food5.shapesize(stretch_wid = 0.4, stretch_len = 0.4)
    x = -280
    y = random.randint(-280, 280)
    pac_s_food5.setposition(x, y)
    pac_s_foods5.append(pac_s_food5)

pac_s_foods6 = []
for _ in range(100):
    pac_s_food6 = turtle.Turtle()
    pac_s_food6.speed(0)
    pac_s_food6.penup()
    pac_s_food6.color('blue')
    pac_s_food6.shape('circle')
    pac_s_food6.shapesize(stretch_wid = 0.4, stretch_len = 0.4)
    x = random.randint(-280, 175)
    y = 200
    pac_s_food6.setposition(x, y)
    pac_s_foods6.append(pac_s_food6)

pac_s_foods7 = []
for _ in range(100):
    pac_s_food7 = turtle.Turtle()
    pac_s_food7.speed(0)
    pac_s_food7.penup()
    pac_s_food7.color('blue')
    pac_s_food7.shape('circle')
    pac_s_food7.shapesize(stretch_wid = 0.4, stretch_len = 0.4)
    x = random.randint(192, 280)
    y = 175
    pac_s_food7.setposition(x, y)
    pac_s_foods7.append(pac_s_food7)

pac_s_foods8 = []
for _ in range(100):
    pac_s_food8 = turtle.Turtle()
    pac_s_food8.speed(0)
    pac_s_food8.penup()
    pac_s_food8.color('blue')
    pac_s_food8.shape('circle')
    pac_s_food8.shapesize(stretch_wid = 0.4, stretch_len = 0.4)
    x = random.randint(12, 159)
    y = 165
    pac_s_food8.setposition(x, y)
    pac_s_foods8.append(pac_s_food8)

pac_s_foods9 = []
for _ in range(100):
    pac_s_food9 = turtle.Turtle()
    pac_s_food9.speed(0)
    pac_s_food9.penup()
    pac_s_food9.color('blue')
    pac_s_food9.shape('circle')
    pac_s_food9.shapesize(stretch_wid = 0.4, stretch_len = 0.4)
    x = random.randint(-280, 110)
    y = -98
    pac_s_food9.setposition(x, y)
    pac_s_foods9.append(pac_s_food9)

pac_s_foods10 = []
for _ in range(100):
    pac_s_food10 = turtle.Turtle()
    pac_s_food10.speed(0)
    pac_s_food10.penup()
    pac_s_food10.color('blue')
    pac_s_food10.shape('circle')
    pac_s_food10.shapesize(stretch_wid = 0.4, stretch_len = 0.4)
    x = 220
    y = random.randint(-250, 110)
    pac_s_food10.setposition(x, y)
    pac_s_foods10.append(pac_s_food10)

pac_s_foods11 = []
for _ in range(100):
    pac_s_food11 = turtle.Turtle()
    pac_s_food11.speed(0)
    pac_s_food11.penup()
    pac_s_food11.color('blue')
    pac_s_food11.shape('circle')
    pac_s_food11.shapesize(stretch_wid = 0.4, stretch_len = 0.4)
    x = random.randint(-250, 220)
    y = -150
    pac_s_food11.setposition(x, y)
    pac_s_foods11.append(pac_s_food11)


ghostenemies = []# ghost enemies
for _ in range(52):#52 of these enemies will be created
    ghostenemy = turtle.Turtle()#Defining ghosts as a Turtle sprite.
    ghostenemy.speed(0)#Ghosts will be at their fastest speed(if additional code was added allowing the ghosts to be movable)
    ghostenemy.penup()#Avoid confusing gameplay by removing tracks left by ghosts
    ghostenemy.color('cyan')#Cyan ghost
    ghostenemy.shape('circle')#Cyan circular ghost that will be stretched out into a pseudo square like geometric figure
    ghostenemy.shapesize(stretch_wid = 0.4, stretch_len = 0.4)
    x = random.randint(-280, 280)#The x value for the ghost's location lies in interval -280 <= x <= -280, where x is an integer. The min x value where ghosts spawn is -280, and the max x value where ghosts spawn is 280
    y = random.randint(-280, 280)#The y value for the ghost's location lies in interval -280 <= y <= -280, where y is an integer. The min y value where ghosts spawn is -280, and the max y value where ghosts spawn is 280
    ghostenemy.setposition(x, y)#Circular ghosts will be placed/spawn on random (x, y) coordinate, where -280 <= x <= 280, where x is an integer, and -280 <= y <= -280, where y is an integer
    ghostenemies.append(ghostenemy)#Circular ghost enemies will be on list circular_ghosts


def pac_movement():#Pacman's movements:
    if pacman.direction == 'up':#If pacman's direction is  up
        y = pacman.ycor()#Getting Pacman's  pretranslated y coordinates
        y += 10
        pacman.sety(y)
    if pacman.direction == 'down': # If pacman's direction is down
        y = pacman.ycor()#Getting Pacman's  pretranslated y coordinates
        y -= 10
        pacman.sety(y)
    if pacman.direction == 'left':#If pacman's direction is  left
        x = pacman.xcor()#Getting Pacman's  pretranslated x coordinates
        x -= 10
        pacman.setx(x)
    if pacman.direction == 'right':#If pacman's direction is right
        x = pacman.xcor()#Getting Pacman's pretranslated x coordinates
        x += 10
        pacman.setx(x)

def upwards_direction():#Function defining upwards direction, which will be called upon key press with the up key
    pacman.direction = 'up'#Pacman's direction will be up
def downwards_direction():#Function defining downwards direction, which will be called upon key press with the up key
    pacman.direction = 'down'#Pacman's direction will be down
def leftwards_direction():#Function defining leftwards direction, which will be called upon key press with the left key
    pacman.direction = 'left'#Pacman's direction will be left
def rightwards_direction():#Function defining rightwards direction, which will be called upon key press with the right key
    pacman.direction = 'right'#Pacman's direction will be right

window.listen()#Listening to overall the entire game inputs, particularly for the key controls
window.onkeypress(upwards_direction, 'Up')#Pacman will go up if up key pressed
window.onkeypress(downwards_direction, 'Down')#Pacman will go down if down key pressed
window.onkeypress(leftwards_direction, 'Left')#Pacman will go left if left key pressed
window.onkeypress(rightwards_direction, 'Right')#Pacman will go right if right key pressed


#Updating in game events
while True:
    window.update()
      #If pacman's location on the x coordinate is greater than 300 or less than -300, and if pacman's y coordinate is greater than 300 or less than -300
    if pacman.xcor() > 280 or pacman.xcor() <-280 or pacman.ycor()>280 or pacman.ycor() < -280:
        pac_s_lives -= 1#Pacman dies
        pen.clear()#Killing pacman
        pen.write('GAMESCORE:{} LIVES REMAINING:{}'.format(gamescore, pac_s_lives), align = 'center', font=('Courier',20))#Rewrite changes in life/scoreboard, that a life has been lost
        time.sleep(1)#Wait 1 second so we can accurately compute lives and to enhance Pacman's death
        pacman.goto(0, 0)#Respawn Pacman

    for pac_s_food in pac_s_foods:
        if pacman.distance(pac_s_food) < 10:
            gamescore += 1
            pen.clear()
            pen.write('GAMESCORE:{} LIVES REMAINING:{}'.format(gamescore, pac_s_lives), align = 'center', font=('Courier',20))
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            pac_s_food.goto(x, y)
    for ghostenemy in ghostenemies:
        if pacman.distance(ghostenemy) < 10:# If the distance between pacman and the circular ghost enemy is less than 10
            pac_s_lives -= 1#Pacman dies
            pen.clear()#Kill pacman
            pacman.goto(0, 0)#Respawn Pacman
            pen.write('GAMESCORE:{} LIVES REMAINING:{}'.format(gamescore, pac_s_lives), align = 'center', font=('Courier',20))
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            ghostenemy.goto(x, y)#Randomply place ghostenemy on coordinate (-280 <= x <= 280, -280 <= y <= 280), where x and y are integers.
            time.sleep(1)#Wait 1 second so we can accurately compute lives and to enhance Pacman's death
    if pac_s_lives == 0:#If Pacman has 0 lives left
        #Reset game(game over)
        gamescore = 0
        pac_s_lives = 3
        pen.clear()
        pen.write('GAMESCORE:{} LIVES REMAINING:{}'.format(gamescore, pac_s_lives), align = 'center', font=('Courier',20))
        pacman.goto(0, 0)#Respawn pacman
        time.sleep(1)#Accurate computation of score and lives
    pac_movement()
