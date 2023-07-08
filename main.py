import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from turtle import Screen

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

gameon = True
while gameon:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 18:
        snake.extend()                                                                                                  #adding a segment to the snake
        food.reposition()
        scoreboard.write_score()
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.game_over()
        gameon = False
    for segment in snake.turtles[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.game_over()
            gameon=False

screen.exitonclick()