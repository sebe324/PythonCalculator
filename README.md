# Python Calculator
A calculator made in python.

This application uses the Reverse Polish Notation for calculations.

The algorithm is written in C++, but the user interface is made in PySimpleGui.
## Calculator in action

![2023-08-14 16-59-44](https://github.com/sebe324/sebe324/assets/58781463/9d1029f9-e40a-4e5a-810c-461375c3ad34)

## Tests
![obraz](https://github.com/sebe324/PythonCalculator/assets/58781463/85233672-9c18-4596-a377-9b123538b6a1)

## Contributing
  - If anyone wants to contribute feel free to do so. Just send a pull request and I will review it.
  - You can check out the issues or the to-do list at the bottom of this readme.
## How to build

### 1. Just building the python code

- Install python
- Install PySimpleGUI
  ```pip install PySimpleGUI```
- Install playsound
```pip install playsound```
- Make sure that the .pyd file and the .py file are in the same folder
- Just do this line in the same directory as the files.
  ```python CalculatorUI.py```
- It should work.


### 2. Building the c++ code and using pybind11
  - This process is quite complicated and I myself had a lot of problems with using pybind.
  - I'm going to leave this [guide](https://learn.microsoft.com/en-us/visualstudio/python/working-with-c-cpp-python-in-visual-studio?view=vs-2022). It does a
    much better job explaining this than I could.
## To do list
- Write the rpn algorithm in C++ [x]
- Write tests to make sure things are running smoothly [x]
- Organize rpn code to be more readable [x]
- Bind the C++ code to python [x]
- Create a GUI [x]
- Add functionality to the GUI [x]
- Fix all the bugs [ ]
- Add documentation [ ]
- Light and dark mode [ ]
- Window confirming if the user wants to exit the calculator [x]
