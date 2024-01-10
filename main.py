from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")


screen.listen()


# The section below controls the movement of the snake.
# Here the idea is to make the last  segment of the snake to move
# to the place of next segment of the snake and so on.
# now what happens with that is , as the head moved ahead
# the body follows behind.
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #collision with food
    if snake.head.distance(food)< 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 295 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    #if head collides with any part of the body
        #trigger game over
    for snake_part in snake.snake_parts[1:]:
        if snake.head.distance(snake_part)< 10 :
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
