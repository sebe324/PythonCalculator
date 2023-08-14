#include <pybind11/pybind11.h>
#include "rpn.h"

namespace py = pybind11;

PYBIND11_MODULE(MyMathLibrary, m) {
    m.def("convertToRPN", &rpn::convertToRPN, R"pbdoc(
        Convert an infix equation to a reverse polish notation.
    )pbdoc");
    m.def("calculateRPN", &rpn::calculateRPN, R"pbdoc(
        Calculate a revelse polish notation equation.
    )pbdoc");
#ifdef VERSION_INFO
    m.attr("__version__") = VERSION_INFO;
#else
    m.attr("__version__") = "dev";
#endif
}