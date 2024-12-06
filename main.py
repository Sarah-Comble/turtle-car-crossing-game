import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Player
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Moving the turtle (only up in this game)
screen.onkey(player.move_turtle, "Up")
screen.listen()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars_forward()
    scoreboard.show_level()

# detect collision
    for cars in car_manager.all_cars:
        if cars.distance(player) < 20 :
            game_is_on = False
            scoreboard.game_over()


# detect a successful crossing
    if player.ycor() > 280:
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()