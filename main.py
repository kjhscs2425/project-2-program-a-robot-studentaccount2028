# Import the robot control commands from the library
from simulator import robot
import time
left, right = robot.sonars()

def drive_forward(distance):
    robot.motors(1, 1, distance)

def drive_backward(distance):
    robot.motors(-1, -1, distance)

def turn_left(distance):
    robot.motors(-1, 1, distance)

def turn_right(distance):
    robot.motors(1, -1, distance)

def check_dist_left():
    left = robot.sonars()
    return left

def check_dist_right():
    right = robot.sonars()
    return right

def movement_check():
    left, right = robot.sonars
    if left >= 3 and right >= 3:
        return True
    else:
        return False

def dance():
    robot.motors(1, 1, 3)
    robot.motors(-1, -1, 3)
    robot.motors(-1, 1, 3)
    robot.motors(1, -1, 3)

number = 2
while number > 0:
    dance()
    number = number - 1

left = check_dist_left()
right = check_dist_right()

if left >= 3 and right >= 3:
    turn_left(180)

if left >= 5 and right >= 3:
    turn_left(180)
    
if left >= 3 and right >= 5:
    turn_left(180)
    
if left >= 3 and right >= 2:
    turn_left(180)
    
if left >= 2 and right >= 3:
    turn_left(180)

user_ask = input("What would you like to do?: ")
go_forward = input("Would you like to go forward?: ")
go_backward = input("Would you like to go forward?: ")
go_left = input("Would you like to go left?: ")
go_right = input("Would you like to go right: ")

if user_ask == "forward":
    drive_forward(2)

if user_ask == "back":
    drive_backward(2)

if user_ask == "left":
    turn_left(2)

if user_ask == "right":
    turn_right(2)

if user_ask == "dance":
    dance()
    
if user_ask == "easteregg":
    print("uh oh!!!")
    dance()
    dance()
    dance()
    dance()
    dance()

