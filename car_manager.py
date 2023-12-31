from turtle import Turtle
import random as rand

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.speed = STARTING_MOVE_DISTANCE
            
    def create_cars(self):
        for i in range(len(COLORS)):
            random_y_pos = rand.randint(-240,240)
            random_x_pos = rand.randint(300,600)
            car = Turtle('square')
            car.color(rand.choice(COLORS))
            car.shapesize(stretch_len=2)
            car.penup()
            car.setheading(180)
            car.goto(x=random_x_pos, y=random_y_pos)
            self.cars.append(car)
        
    def move_car(self):
        for car in self.cars:
            if car.xcor() < 350:
                car.forward(self.speed)
    
    def collision(self, turtle):
        for car in self.cars:
            if turtle.distance(car) < 20:
                return True
        return False
    
    def increase_speed(self):
        self.speed += MOVE_INCREMENT