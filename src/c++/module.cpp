#include <pybind11/pybind11.h>
#include "rpn.h"

namespace py = pybind11;

PYBIND11_MODULE(MyMathLibrary, m)
{
	m.doc() = "pybind11module";
	m.def("convertToRPN", &rpn::convertToRPN, "Convert an infix equation to a reverse polish notation");
	m.def("calculateRPN", &rpn::calculateRPN, "Calculate an equation written in reverse polish notation");
	m.def("setUseRadians",&rpn::setUseRadians, "Use radians if true or degrees if false");
#ifdef VERSION_INFO
	m.attr("__version__") = VERSION_INFO;
#else
	m.attr("__version__") = "dev";
#endif
}
