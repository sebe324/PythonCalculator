import MyMathLibrary as mml
import PySimpleGUI as sg
import sys
from layouts import *
from misc import *

window=sg.Window("Calculator",layout,icon="icon.ico",background_color='#909090', margins=(0,0), size=(700, 650), enable_close_attempted_event=True)
#window.read()
#move_center(window)
equation=""
operators = ("+","-","x","/","^")
calculatorButtons=('0','1','2','3','4','5','6','7','8','9', 'x','root','(',')','+','-','=','/','.','sin(x)','cos(x),tg(x),ctg(x),abs(x)')

isSoundOn=True
isExitWindowOn=True
isScienceMode = False

index = len(equation)
while True:
    event, values = window.read()
    isExitWindowOn=values['exit_window_checkbox']
    isSoundOn=values['sound_checkbox']
    isScienceMode=values['science_mode_checkbox']
    if(len(event.strip()) != 0 and isSoundOn):
        click_sound()
    if (event == "OFF" or event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT):
        if(isExitWindowOn): exit_confirmation(window)
        else: window.close()
    elif event == "<-":
        if(index>0): index-=1
    elif event == "->":
        if(index<len(equation)): index+=1
    elif event.isdigit():
        equation = insert_str(equation,event,index)
        index+=1
    elif event == "AC":
        equation=""
        index=0
    elif event == "DEL":
        x=list(equation)
        if(len(x)>0):
            print(index-1)
            del x[index-1]
            if(index==len(equation)):
                index-=1
        equation="".join(x)
    elif event == "sin(x)":
        equation= insert_str(equation,"sin()",index)
        index+=5
    elif event == "cos(x)":
        equation= insert_str(equation,"cos()",index)
        index+=5
    elif event == "tg(x)":
        equation= insert_str(equation,"tg()",index)
        index+=5
    elif event == "ctg(x)":
        equation= insert_str(equation,"ctg()",index)
        index+=5
    elif event == "abs(x)":
        equation= insert_str(equation,"abs()",index)
        index+=5
    elif event =="x":
        equation = insert_str(equation,"*",index)
        index+=1
    elif event in operators:
        equation = insert_str(equation,event,index)
        index+=1
    elif event in ["(", ")", "."]:
        equation = insert_str(equation,event,index)
        index+=1
    elif event == "root":
        equation = insert_str(equation,"@",index)
        index+=1
    elif event == "calculatorBtn":
        window['LayoutC'].update(visible=False)
        window['LayoutS'].update(visible=True)
    elif event == "settingsBtn":
        window['LayoutS'].update(visible=False)
        if(isScienceMode):
            scienceModeOn(True, window)
            window['LayoutC'].update(visible = True)
        else:
            scienceModeOn(False, window)
            window['LayoutC'].update(visible = True)
    elif event == "=":
        if(equation==""): 
            equation="0"
            index=1
        convertedEquation=mml.convertToRPN(equation)
        equation=str(mml.calculateRPN(convertedEquation))
        index=len(equation)
    window['output'].update(equation)
    if(event  in calculatorButtons):
        tmp=mml.convertToRPN(equation)
        x=str(mml.calculateRPN(tmp))
        window['current_output'].update(x)
window.close()
sys.exit()