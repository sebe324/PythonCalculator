import MyMathLibrary as mml
import PySimpleGUI as sg
import sys
from layouts import *
from misc import *

window=sg.Window("Calculator",layout,icon="icon.ico",background_color='#909090', margins=(0,0), enable_close_attempted_event=True)
equation=""
operators = ("+","-","x","/","^")
calculatorButtons=('0','1','2','3','4','5','6','7','8','9', 'x','root','(',')','+','-','=','/','.')

while True:
    event, values = window.read()

    if event == "OFF" or event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
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
    elif event == "calculatorBtn":
        window['LayoutC'].update(visible=False)
        window['LayoutS'].update(visible=True)
        print("test")
    elif event == "settingsBtn":
        window['LayoutC'].update(visible=True)
        window['LayoutS'].update(visible=False)
    elif event == "=":
        if(equation==""): equation="0"
        convertedEquation=mml.convertToRPN(equation)
        equation=str(mml.calculateRPN(convertedEquation))
    window['output'].update(equation)
    if(event  in calculatorButtons):
        tmp=mml.convertToRPN(equation)
        x=str(mml.calculateRPN(tmp))
        window['current_output'].update(x)
window.close()
sys.exit()