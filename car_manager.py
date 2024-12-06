import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
POSITIONS = [(300, 100), (300, 150), (300, 200), (300, 250), (300, 50), (300, 0), (300, -50), (300, -100), (300, -150), (300, -200), (300, -250)]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        # super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
        # new_car.goto(random.choice(POSITIONS))
            new_car.goto(300, random.randint(-250, 250), )
            self.all_cars.append(new_car)

    def move_cars_forward(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
