from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

#setting up the screen display
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Epic Snake Game")
screen.tracer(0)

#creating all the objects
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

#get screen to listen for keystrokes (functions used from the snake class)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 12:
        food.refresh()
        snake.extend()
        scoreboard.score_increase()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()



    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()






screen.exitonclick()