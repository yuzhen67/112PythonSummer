from stanfordkarel import *
import os

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def main():  #函式，方法
    """ Karel code goes here! """
    move()
    pick_beeper()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    move()
    put_beeper()
    move()
    pass


if __name__ == "__main__":
    run_karel_program(os.path.join(os.getcwd(), 'worlds/karel_01'))