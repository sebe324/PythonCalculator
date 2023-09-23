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
  #### CMake
  - Make sure you have cmake and pybind11 installed.
  - Go to the c++ folder. In the project directory do: ```cd src/c++```
  - Sometimes CMake can have problems with finding pybind11. To fix this try this:
    - In console ```pip show pybind```.
    - In CMakeLists.txt change [LOCATION] to the location you get from the command.
    - If your path contains single escape characters ```\``` make sure to replace them with ```\\```
    - ```cmake .```
    - ```cmake --build .```
    - The .pyd file should be located in one of the folders created.
    - Now you can move the .pyd file to the python src folder and build the rest.
  #### Visual Studio
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