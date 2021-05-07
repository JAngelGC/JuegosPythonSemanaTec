from turtle import *
from random import randrange
from freegames import square, vector
import random


rs=random.randint(1,5)
rf=random.randint(1,5)

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

if rs == 1:
    cs='black'
elif(rs==2):
    cs= 'blue'
elif(rs==3):
    cs='cyan'
elif(rs==4):
    cs='yellow'
else:
    cs= 'purple'


if rf == 1:
    cf='limegreen'
elif(rf==2):
    cf='orange'
elif(rf==3):
    cf='brown'
elif(rf==4):
    cf='olive'
else:
    cf= 'gray'

print(cs, rs, cf, rf)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:

        # Adding random movement to the food for each movement of the snake
        if abs(food.x) != 15*10:
            food.x = food.x + randrange(-1, 2) * 10

        if abs(food.y) != 15*10:
            food.y = food.y + randrange(-1, 2) * 10


        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, cs)

    # Here is where the food is make it
    square(food.x, food.y, 9, cf)

    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
