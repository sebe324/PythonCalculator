# Import necessary libraries
import MyMathLibrary as mml
import PySimpleGUI as sg
import sys
from layouts import *
from misc import *

# Create the main window for the calculator
window = sg.Window("Calculator", layout, icon="icon.ico", background_color='#909090', margins=(0, 0), size=(700, 650), enable_close_attempted_event=True)

# Initialize variables
equation = "|"
operators = ("+", "-", "x", "/", "^")
calculatorButtons = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'x', 'root', '(', ')', '+', '-', '=', '/', '.', 'sin(x)', 'cos(x)', 'tg(x)', 'ctg(x)', 'abs(x)', 'DEL', '<-','->')

isSoundOn = True
isExitWindowOn = True
isScienceMode = False
useRadians = False
index = 0

# Main event loop
while True:
    event, values = window.read()

    # Update settings based on user input
    isExitWindowOn = values['exit_window_checkbox']
    isSoundOn = values['sound_checkbox']
    isScienceMode = values['science_mode_checkbox']
    useRadians = values['use_radians_checkbox']

    mml.setUseRadians(useRadians)
    # Play a click sound if enabled and an event occurred
    if (len(event.strip()) != 0 and isSoundOn):
        click_sound()

    # Handle window close events
    if (event == "OFF" or event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT):
        if (isExitWindowOn):
            exit_confirmation(window)
        else:
            window.close()
    elif event == "<-":
        if (index > 0):
            index -= 1
    elif event == "->":
        if (index < len(equation)):
            index += 1
    elif event.isdigit():
        equation = insert_str(equation, event, index)
        index += 1
    elif event == "AC":
        equation = ""
        index = 0
    elif event == "DEL":
        x = list(equation)
        if (len(x) > 0):
            if(index-1>=0):
                del x[index - 1]
                index -= 1
        equation = "".join(x)
    # Handle trigonometric and other special functions
    elif event == "sin(x)":
        equation = insert_str(equation, "sin()", index)
        index += 5
    elif event == "cos(x)":
        equation = insert_str(equation, "cos()", index)
        index += 5
    elif event == "tg(x)":
        equation = insert_str(equation, "tg()", index)
        index += 4
    elif event == "ctg(x)":
        equation = insert_str(equation, "ctg()", index)
        index += 5
    elif event == "abs(x)":
        equation = insert_str(equation, "abs()", index)
        index += 5
    elif event == "x":
        equation = insert_str(equation, "*", index)
        index += 1
    # Handle operators and special characters
    elif event in operators:
        equation = insert_str(equation, event, index)
        index += 1
    elif event in ["(", ")", "."]:
        equation = insert_str(equation, event, index)
        index += 1
    elif event == "root":
        equation = insert_str(equation, "√", index)
        index += 1
    # Handle mode switches
    elif event == "calculatorBtn":
        window['LayoutC'].update(visible=False)
        window['LayoutS'].update(visible=True)
    elif event == "settingsBtn":
        window['LayoutS'].update(visible=False)
        if (isScienceMode):
            scienceModeOn(True, window)
            window['LayoutC'].update(visible=True)
        else:
            scienceModeOn(False, window)
            window['LayoutC'].update(visible=True)
    # Handle calculation
    elif event == "=":
        if (equation == "|"):
            equation = "|"
            index = 0
        else:    
            tmp_equation = equation.replace('|','')
            tmp_equation = tmp_equation.replace('√','@')
            convertedEquation = mml.convertToRPN(tmp_equation)
            equation = str(mml.calculateRPN(convertedEquation))+"|"
            index = len(equation)
    equation = equation.replace('|','')
    equation = insert_str(equation, "|",index)
    print(index)
    # Update the displayed equation and result
    window['output'].update(equation)
    if (event in calculatorButtons):
        tmp_equation=equation.replace('|','')
        tmp_equation=tmp_equation.replace('√','@')
        tmp = mml.convertToRPN(tmp_equation)
        x = str(mml.calculateRPN(tmp))
        window['current_output'].update(x)

# Close the window and exit the application
window.close()
sys.exit()
