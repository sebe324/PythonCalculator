#pragma once
#include <string>
#include <vector>
#include <map>

namespace rpn {
	bool isNumber(const char value);
	bool isOperator(const char value);
	bool isLetter(const char value);

	double calculate(double a, double d, char op);
	double calculateFunc(double a, const std::string& funcName);
	std::string convertToRPN(const std::string& str);

	double calculateRPN(const std::string& str);

	const std::vector<char> digits = { '0','1','2','3','4','5','6','7','8','9' };
	const std::vector<char> operators = { '+','-','*','/','^','@'}; //@ is the root operator
	const std::map<std::string, unsigned> operatorOrder = { {"+",1},{"-",1},{"*",2},{"/",2},{"^",3},{"@",3} };
}