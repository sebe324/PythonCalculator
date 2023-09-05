import PySimpleGUI as sg
from playsound import playsound
import threading
import sys
from layouts import *
def exit_confirmation(main_window):
    exit_window = sg.Window("Do you want to exit?", [[sg.Button("Stay", **b_style2), sg.Button("Exit",**b_style3)]],enable_close_attempted_event=True)
    while True:
        exit_event, exit_values = exit_window.read()
        if exit_event == "Exit":
            exit_window.close()
            main_window.close()
            sys.exit()
        elif exit_event == 'Stay' or exit_event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
            break
    exit_window.close()

def click_sound():
    t = threading.Thread(target=playsound, args=("./click.mp3",))
    t.start()
