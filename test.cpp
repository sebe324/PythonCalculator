#include <iostream>
#include <windows.h>

#include "rpn.h"

using namespace rpn;


bool rpnTest(const std::string& equationInfix, double expectedResult) {
	HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleTextAttribute(hConsole, 11);
	std::cout << "STARTING TEST" << std::endl;
	SetConsoleTextAttribute(hConsole, 15);
	std::cout << "Test sample: " << equationInfix << std::endl;
	std::string test = convertToRPN(equationInfix);
	std::cout << "Conversion to the RPN: " << test << std::endl;
	double result = calculateRPN(test);
	std::cout << "Calculating the result: " << result << std::endl;
	std::cout << "Expected result: " << expectedResult << std::endl;
	if (expectedResult == result) {
		SetConsoleTextAttribute(hConsole, 10);
		std::cout << "TEST SUCCESSFULL!" << std::endl;
		SetConsoleTextAttribute(hConsole, 15);
		return true;
	}
	else {
		SetConsoleTextAttribute(hConsole, 12);
		std::cout << "TEST FAILED :(" << std::endl;
		SetConsoleTextAttribute(hConsole, 15);
		return false;
	}
}
int main() {

	rpnTest("3 + 2 * 5",13.0);
	rpnTest("2 * (5 + 2)",14.0);
	rpnTest("(7 + 3) * (5 - 2) ^ 2",90.0);
	rpnTest("4 / (3 - 1) ^ (2 * 3) ",0.0625);
	rpnTest("( ( 5 - 2 ) ^ ( 3 + 1 ) / ( 2 + 1 ) + 12 ) * 21",819.0);
	return 0;
}