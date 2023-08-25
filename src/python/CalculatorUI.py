import MyMathLibrary as mml
import PySimpleGUI as sg
import sys
from playsound import playsound
import threading

sg.set_options(font=('Franklin Gothic Book', 24))
bStyle1 = {'size':(5,2),'button_color':("#00b894","#dfe6e9")}
bStyle2 = {'size':(5,2),'button_color':("white","#0984e3")}
bStyle3 = {'size':(5,2),'button_color':("white","tomato")}
bStyle4 = {'size':(9,2),'button_color':("#00b894","#dfe6e9")}
font = ("Arial", 13)
layout=[
    [sg.Text('Calculator', size=(30,1), justification = 'right',background_color='#909090')],
    [sg.Text('0.00000', key='output', size=(30,1), justification = 'right', background_color='white', text_color='black',pad=(5,0))],
    [sg.Text('0.00000', key='current_output', size=(63,1), justification = 'right', background_color='#909090', text_color='black',pad=(5,0),font=font)],
    [sg.Button("7",**bStyle1),sg.Button("8",**bStyle1),sg.Button("9",**bStyle1),sg.Button("DEL",**bStyle2),sg.Button("AC",**bStyle2)],
    [sg.Button("4",**bStyle1),sg.Button("5",**bStyle1),sg.Button("6",**bStyle1),sg.Button("x",**bStyle1),sg.Button("/",**bStyle1)],
    [sg.Button("1",**bStyle1),sg.Button("2",**bStyle1),sg.Button("3",**bStyle1),sg.Button("+",**bStyle1),sg.Button("-",**bStyle1),],
    [sg.Button("0",**bStyle1),sg.Button(".",**bStyle1),sg.Button("=",**bStyle1),sg.Button("^",**bStyle1),sg.Button("OFF",**bStyle3),],
    [sg.Button("(",**bStyle4),sg.Button(")",**bStyle4),sg.Button("√", key="root",**bStyle4)]
    ]

def exit_confirmation(main_window):
    exit_window = sg.Window("Do you want to exit?", [[sg.Button("Stay", **bStyle2), sg.Button("Exit",**bStyle3)]], disable_close=True)
    while True:
        exit_event, exit_values = exit_window.read()
        if exit_event == "Exit":
            exit_window.close()
            main_window.close()
            sys.exit()
        elif exit_event == 'Stay':
            break
    exit_window.close()

def click_sound():
    t = threading.Thread(target=playsound, args=("./click.mp3",))
    t.start()

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