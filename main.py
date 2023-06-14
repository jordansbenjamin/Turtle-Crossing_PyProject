import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing')
screen.tracer(0)

turtle = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move, "Up")

game_is_on = True
counter = 0
generate_new_cars = 6

while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Generate new set of cars after 6 passes of the loop
    if counter % generate_new_cars == 0:
        car.create_cars()
    
    car.move_car()
    counter += 1

    # Detects turtle collision with cars
    if car.collision(turtle):
        # Display game over
        game_is_on = False

    # Detect when turtle reaches the finish line
    if turtle.reached_finish_line():
        turtle.reset()
        # Update level
        car.increase_speed()
        
screen.exitonclick()
