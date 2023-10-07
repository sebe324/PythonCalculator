cmake_minimum_required(VERSION 3.18)
project(MyMathLibrary LANGUAGES CXX)
find_package(Python COMPONENTS Interpreter Development)
#[[
    In console do: pip show pybind11.
    then swap [LOCATION] to the location that the command returns.
    It should hopefully work
]]

set(PYBIND11_LOCATION [LOCATION])

set(CMAKE_PREFIX_PATH ${PYBIND11_LOCATION}/pybind11/share/cmake/pybind11)

find_package(pybind11 CONFIG REQUIRED)

Python_add_library(MyMathLibrary module.cpp rpn.cpp)
target_link_libraries(MyMathLibrary PRIVATE pybind11::headers)
set_target_properties(MyMathLibrary PROPERTIES
                                INTERPROCEDURAL_OPTIMIZATION ON
                                CXX_VISIBILITY_PRESET ON
                                VISIBILITY_INLINES_HIDDEN ON
                                OUTPUT_NAME MyMathLibrary)