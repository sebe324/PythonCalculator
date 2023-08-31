import MyMathLibrary as mml
import PySimpleGUI as sg
import sys
from layouts import *
from misc import *

window=sg.Window("Calculator",layout,icon="icon.ico",background_color='#909090', margins=(0,0), disable_close=True)
equation=""
operators = ("+","-","x","/","^")
while True:
    event, values = window.read()
    if(len(event.strip()) != 0):
        click_sound()

    if event == "OFF":
        exit_confirmation(window)
    elif event.isdigit():
        equation += event
    elif event == "AC":
        equation=""
    elif event == "DEL":
        x=list(equation)
        if(len(x)>0):
            x.pop()
        equation="".join(x)
    elif event =="x":
        equation+="*"
    elif event in operators:
        equation += event
    elif event in ["(", ")", "."]:
        equation += event
    elif event == "root":
        equation+="r"
    elif event == "=":
        if(equation==""): equation="0"
        convertedEquation=mml.convertToRPN(equation)
        equation=str(mml.calculateRPN(convertedEquation))
    window['output'].update(equation)
    if(event not in operators):
        tmp=mml.convertToRPN(equation)
        x=str(mml.calculateRPN(tmp))
        window['current_output'].update(x)
window.close()
sys.exit()