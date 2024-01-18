from pynput.mouse import Button, Controller
from time import sleep
from random import randint
from screeninfo import get_monitors

AUTOCLICK_SPEED = 5
AUTOMOVE_SPEED = 0.025
MAX_WIDTH = 0
MAX_HEIGHT = 0

mouse = Controller()
monitors = get_monitors()

def menu():
    print("=== Python Autoclick/Automove script ===")
    print("Used for keep an activity in your pc.")
    print("1. Autoclick")
    print("2. Automove")
    choice = -1
    while(choice != "1" and choice != "2"):
        choice = input("Please choose a mod: ")
        if(not(choice.isdigit())):
            print("Please type a valid mod.")
    return int(choice)

def auto_click():
    while(1):
        mouse.press(Button.left)
        mouse.release(Button.left)
        print(f"Mouse pressed")
        sleep(AUTOCLICK_SPEED)

def auto_move():
    while(1):
        x = randint(0, MAX_WIDTH)
        y = randint(0, MAX_HEIGHT)
        mouse.position = (x, y)
        sleep(AUTOMOVE_SPEED)

def start(choice):
    if(choice == 1): auto_click()
    elif(choice == 2): auto_move()
    else: print("This mod isn't valid (valid mod: 1 or 2)")

def set_max_size():
    global MAX_HEIGHT, MAX_WIDTH
    for monitor in monitors:
        MAX_WIDTH += monitor.width
        MAX_HEIGHT += monitor.height

def main():
    choice = 0
    choice = menu()
    set_max_size()
    start(choice)

main()

