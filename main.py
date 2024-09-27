import turtle
from turtle import Turtle, Screen,onkey,clear
import random
import time
from snake import Snake
from food import Food
from scoryboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)






snake = Snake()
food = Food()
scoreboard = Scoreboard()
game_is_on = True


while game_is_on:
    time.sleep(0.1)
    snake.move()
    screen.update()
    random_x = random.randint(-290, 290)
    random_y = random.randint(-290, 290)
    if snake.head.distance(food) <= 15:

        scoreboard.increase_score()

        food.goto(random_x,random_y)
        screen.tracer(0)
        snake.add_snake()
    for seg in snake.segments:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()


    for int in range(-300,300):
      if snake.head.distance(-300,int)<=10:
          snake.reset()
          scoreboard.reset()
      elif snake.head.distance(300, int)<=10:
          snake.reset()
          scoreboard.reset()
      elif snake.head.distance(int,-300)<=10:
          snake.reset()
          scoreboard.reset()
      elif snake.head.distance(int, 300)<=10:
          snake.reset()
          scoreboard.reset()








screen.exitonclick()






















