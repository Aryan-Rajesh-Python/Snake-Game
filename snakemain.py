from turtle import Turtle,Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("brown")
screen.title("My Animation Snake Game")
screen.tracer(0)
snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.up,"u")
screen.onkey(snake.down,"d")
screen.onkey(snake.left,"l")
screen.onkey(snake.right,"r")
game_on=True
while(game_on):
    screen.update()
    time.sleep(0.5)
    snake.move()
    if(snake.head.distance(food)<15):
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if(snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290):
        game_on=False
        scoreboard.game_over()
    for segment in snake.segment:
        if(segment==snake.head):
            pass
        elif(snake.head.distance(segment)<10):
            game_on=False
            scoreboard.game_over()
screen.exitonclick()