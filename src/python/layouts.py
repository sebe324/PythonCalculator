# Import the PySimpleGUI library and set font options
import PySimpleGUI as sg
sg.set_options(font=('Franklin Gothic Book', 24))

# Define button styles using dictionaries
b_style1 = {'size':(5,2),'button_color':("#00b894","#dfe6e9")}
b_style2 = {'size':(5,2),'button_color':("white","#0984e3")}
b_style3 = {'size':(5,2),'button_color':("white","tomato")}
b_style4 = {'size':(9,2),'button_color':("#00b894","#dfe6e9")}
b_style_settings = {'button_color':('#303030','#404040')}
font = ("Arial", 13)

# Define styles for light and dark modes
light_mode = {
    'background': '#ffffff',
    'text': '#000000',
    'button': ('#000000', '#dfe6e9'),
    'input': ('#000000', '#ffffff')
}

dark_mode = {
    'background': '#303030',
    'text': '#ffffff',
    'button': ('#ffffff', '#404040'),
    'input': ('#ffffff', '#303030')
}

# Define the path to the gear icon image
gear_icon_path = './gear.png'

# Define the layout for the calculator window
layout_calculator = [
    [sg.Button(image_filename=gear_icon_path, key='calculatorBtn', **b_style_settings), sg.Text('Calculator', size=(30, 1), background_color='#909090')],
    [sg.Text('|', key='output', size=(30, 1), justification='right', background_color='white', text_color='black', pad=(5, 0))],
    [sg.Button("<-"), sg.Button("->"), sg.Text('0.00000', key='current_output', size=(63, 1), background_color='#909090', text_color='black', pad=(5, 0), font=font)],
    [sg.Button("7", **b_style1), sg.Button("8", **b_style1), sg.Button("9", **b_style1), sg.Button("DEL", **b_style2), sg.Button("AC", **b_style2), sg.Button("sin(x)", visible=False, **b_style1)],
    [sg.Button("4", **b_style1), sg.Button("5", **b_style1), sg.Button("6", **b_style1), sg.Button("x", **b_style1), sg.Button("/", **b_style1), sg.Button("cos(x)", visible=False, **b_style1)],
    [sg.Button("1", **b_style1), sg.Button("2", **b_style1), sg.Button("3", **b_style1), sg.Button("+", **b_style1), sg.Button("-", **b_style1), sg.Button("tg(x)", visible=False, **b_style1)],
    [sg.Button("0", **b_style1), sg.Button(".", **b_style1), sg.Button("=", **b_style1), sg.Button("^", **b_style1), sg.Button("OFF", **b_style3), sg.Button("ctg(x)", visible=False, **b_style1)],
    [sg.Button("(", **b_style4), sg.Button(")", **b_style4), sg.Button("√", key="root", **b_style4), sg.Button("abs(x)", visible=False, **b_style1)]
]

# Define the layout for the settings window
layout_settings = [
    [sg.Button(image_filename=gear_icon_path, key='settingsBtn', **b_style_settings)],
    [sg.Checkbox("Dark mode", enable_events=True, key='dark_mode_checkbox', background_color='#909090')],
    [sg.Checkbox("Sound", default=True, key='sound_checkbox', background_color="#909090")],
    [sg.Checkbox("Science Mode", enable_events=False, key='science_mode_checkbox', background_color="#909090")],
    [sg.Checkbox("Exit Window", default=True, key='exit_window_checkbox', background_color="#909090")],
    [sg.Checkbox("Use radians", default=False, key='use_radians_checkbox', background_color="#909090")]
]

# Initialize the currentLayout variable
currentLayout = 0

# Create the main layout using columns for calculator and settings
layout = [
    [sg.Column(layout_calculator, visible=True, key='LayoutC', background_color='#909090'),
     sg.Column(layout_settings, visible=False, key="LayoutS", background_color='#909090')]
]

# Function to toggle the visibility of science mode buttons
def scienceModeOn(b, window):
    window['sin(x)'].update(visible=b)
    window['cos(x)'].update(visible=b)
    window['tg(x)'].update(visible=b)
    window['ctg(x)'].update(visible=b)
    window['abs(x)'].update(visible=b)

# Function to apply theme
def apply_theme(window, theme):
    window['LayoutC'].Widget.config(bg=theme['background'])
    window['LayoutS'].Widget.config(bg=theme['background'])
    for key in window.AllKeysDict:
        element = window[key]
        if isinstance(element, sg.Button):
            element.update(button_color=theme['button'])
        elif isinstance(element, sg.Text):
            element.update(background_color=theme['background'], text_color=theme['text'])
        elif isinstance(element, sg.InputText):
            element.update(background_color=theme['input'][1], text_color=theme['input'][0])

if __name__ == "__main__":
    # Create the window for testing
    window = sg.Window('Calculator', layout, finalize=True)
    
    # Apply initial light theme
    apply_theme(window, light_mode)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'dark_mode_checkbox':
            if values['dark_mode_checkbox']:
                apply_theme(window, dark_mode)
            else:
                apply_theme(window, light_mode)
        # Handle other events...

    window.close()
