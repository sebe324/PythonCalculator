#pragma once
#include <string>
#include <vector>
#include <map>

namespace rpn {
	bool isNumber(const char value);
	bool isOperator(const char value);

	double calculate(double a, double d, char op);

	std::string convertToRPN(const std::string& str);

	double calculateRPN(const std::string& str);

	const std::vector<char> digits = { '0','1','2','3','4','5','6','7','8','9' };
	const std::vector<char> operators = { '+','-','*','/','^' };
	const std::map<std::string, unsigned> operatorOrder = { {"+",1},{"-",1},{"*",2},{"/",2},{"^",3} };
}