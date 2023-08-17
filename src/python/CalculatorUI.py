import MyMathLibrary as mml
import PySimpleGUI as sg
import sys 
test = mml.convertToRPN("-3+2")

#print(mml.calculateRPN(test))

sg.set_options(font=('Franklin Gothic Book', 24))
bStyle1 = {'size':(5,2),'button_color':("#00b894","#dfe6e9")}
bStyle2 = {'size':(5,2),'button_color':("white","#0984e3")}
bStyle3 = {'size':(5,2),'button_color':("white","tomato")}
bStyle4 = {'size':(14,2),'button_color':("#00b894","#dfe6e9")}
font = ("Arial", 13)
layout=[
    [sg.Text('Calculator', size=(30,1), justification = 'right',background_color='#909090')],
    [sg.Text('0.00000', key='output', size=(30,1), justification = 'right', background_color='white', text_color='black',pad=(5,0))],
    [sg.Text('0.00000', key='current_output', size=(63,1), justification = 'right', background_color='#909090', text_color='black',pad=(5,0),font=font)],
    [sg.Button("7",**bStyle1),sg.Button("8",**bStyle1),sg.Button("9",**bStyle1),sg.Button("DEL",**bStyle2),sg.Button("AC",**bStyle2)],
    [sg.Button("4",**bStyle1),sg.Button("5",**bStyle1),sg.Button("6",**bStyle1),sg.Button("x",**bStyle1),sg.Button("/",**bStyle1)],
    [sg.Button("1",**bStyle1),sg.Button("2",**bStyle1),sg.Button("3",**bStyle1),sg.Button("+",**bStyle1),sg.Button("-",**bStyle1),],
    [sg.Button("0",**bStyle1),sg.Button(".",**bStyle1),sg.Button("^",**bStyle1),sg.Button("=",**bStyle1),sg.Button("OFF",**bStyle3),],
    [sg.Button("(",**bStyle4),sg.Button(")",**bStyle4)]
    ]


window=sg.Window("Calculator",layout,icon="icon.ico",background_color='#909090', margins=(0,0))
equation=""
operators = ("+","-","x","/","^")
while True:
    event, values = window.read()
    if event == "OFF" or event ==sg.WIN_CLOSED:
        break
    elif event == "0":
        equation+="0"
    elif event == "1":
        equation+="1"
    elif event == "2":
        equation+="2"
    elif event == "3":
        equation+="3"
    elif event == "4":
        equation+="4"
    elif event == "5":
        equation+="5"
    elif event == "6":
        equation+="6"
    elif event == "7":
        equation+="7"
    elif event == "8":
        equation+="8"
    elif event == "9":
        equation+="9"
    elif event == "AC":
        equation=""
    elif event == "DEL":
        x=list(equation)
        if(len(x)>0):
            x.pop()
        equation="".join(x)
    elif event =="+":
        equation+="+"
    elif event =="-":
        equation+="-"
    elif event =="x":
        equation+="*"
    elif event =="/":
        equation+="/"
    elif event == "^":
        equation+="^"
    elif event == ".":
        equation+="."
    elif event == "(":
        equation+="("
    elif event == ")":
        equation+=")"
    elif event == "=":
        if(equation==""): equation="0"
        convertedEquation=mml.convertToRPN(equation)
        equation=str(mml.calculateRPN(convertedEquation))
    window['output'].update(equation)
    if(event not in operators):
        print(event not in operators)
        tmp=mml.convertToRPN(equation)
        x=str(mml.calculateRPN(tmp))
        window['current_output'].update(x)
window.close()
sys.exit()