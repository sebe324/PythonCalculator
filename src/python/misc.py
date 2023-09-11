import PySimpleGUI as sg
from playsound import playsound
import threading
import sys
from layouts import *

# Function to display an exit confirmation window
def exit_confirmation(main_window):
    exit_window = sg.Window("Do you want to exit?", [[sg.Button("Stay", **b_style2), sg.Button("Exit",**b_style3)]], enable_close_attempted_event=True)
    
    while True:
        exit_event, exit_values = exit_window.read()
        if exit_event == "Exit":
            exit_window.close()
            main_window.close()
            sys.exit()
        elif exit_event == 'Stay' or exit_event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
            break
    exit_window.close()

# Function to play a click sound on a separate thread
def click_sound():
    t = threading.Thread(target=playsound, args=("./click.mp3",))
    t.start()

# Function to insert a string into another string at a specified index
def insert_str(string, str_to_insert, index):
    return string[:index] + str_to_insert + string[index:]

# Function to remove a character from a string at a specified index
def remove(s, indx):
    return ''.join(x for x in s if s.index(x) != indx)

# Function to move a window to the center of the screen
def move_center(window):
    screen_width, screen_height = window.get_screen_dimensions()
    win_width, win_height = window.size
    x, y = (screen_width - win_width)//2, (screen_height - win_height)//2
    window.move(x, y)
