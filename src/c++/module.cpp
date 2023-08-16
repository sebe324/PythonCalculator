#include <pybind11/pybind11.h>
#include "rpn.h"

namespace py = pybind11;

PYBIND11_MODULE(huj, m)
{
	m.doc() = "pybind11module";
	m.def("convertToRPN", &rpn::convertToRPN, "Convert an infix equation to a reverse polish notation");
	m.def("calculateRPN", &rpn::calculateRPN, "Calculate an equation written in reverse polish notation");

#ifdef VERSION_INFO
	m.attr("__version__") = VERSION_INFO;
#else
	m.attr("__version__") = "dev";
#endif
}