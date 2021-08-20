from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=300,height=300)
screen.bgcolor("black")
screen.title("SNAKE_GAME")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(0.3)
  snake.move()
  
  #make food change position
  if snake.head.distance(food) < 15:
    snake.extend()
    food.refresh()
    score.increase_score()

#make coolided when sanke hit the wall
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() < -280:  
    game_is_on = False
    score.game_over()

  #make collide if snake it its own tail
  for segment in snake.segments:
    if segment == snake.head:
      pass
    elif snake.head.distance(segment) < 10:
      game_is_on = False 
      score.game_over()
