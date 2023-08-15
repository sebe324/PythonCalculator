#include "rpn.h"

#include <stack>
#include <algorithm>
#include <iostream>
#include <math.h>

bool rpn::isNumber(const char input) {
	return (input >= 48 && input <= 57) || input == '.';
}

bool rpn::isOperator(const char value) {
	return std::find(operators.begin(), operators.end(), value) != operators.end();
}

double rpn::calculate(double a, double b, char op) {
	switch (op) {
	case '+':
		return b + a;
		break;
	case '-':
		return b - a;
		break;
	case '*':
		return b * a;
		break;
	case '/':
		if (b == 0.0) throw std::exception("dont divide by 0!");
		return b / a;
		break;
	case '^':
		return pow(b, a);
		break;
	}
}

std::string rpn::convertToRPN(const std::string& str)
{
	std::string input(str);
	std::string result = "";
	std::stack<std::string> s;
	input.erase(std::remove(input.begin(), input.end(), ' '), input.end()); //remove all spaces
	std::replace(input.begin(), input.end(), 'x', '*'); //some people may like to use x instead of * to multiply
	std::replace(input.begin(), input.end(), ':', '/'); //same goes with :
	unsigned inputSize = input.length();

	//If a negative number n is present change it to (0-n)
	//example 1: 5* -3 = 5*(0-3)
	//example 2: -12+5 = (0-12)+5

	//If a minus sign is present before parinthesis -(equation) change it to (0-(equation))

	//example 1: 3*-(3+3)=3*(0-(3+3))

	for (unsigned i = 0; i < inputSize; i++) {
		if (input[i] == '-' && inputSize - 1 > i && isNumber(input[i + 1])) {
			input.insert(i, "0");
			input.insert(i, "(");
			i += 2;
			inputSize += 2;
			for (unsigned j = i + 1; j <= inputSize; j++) {
				if (j == inputSize) {
					input.insert(j, ")");
					inputSize++;
					break;
				}
				if (!isNumber(input[j])) {
					input.insert(j, ")");
					inputSize++;
					i++;
					break;
				}
			}
		}
		else if (input[i] == '-' && inputSize - 1 > i && input[i + 1] == '('){
			input.insert(i, "0");
			input.insert(i, "(");
			i += 2;
			inputSize += 2;
			for (unsigned j = i + 2; j < inputSize; j++) {
				//check if there is a parinthesis inside a parinthesis
				//example 1: -(5+(3*2)) = (0-(5+(3*2)))
				unsigned parinthesis_begin_count = 1;
				unsigned parinthesis_end_count = 0;
				if (input[j] == '(') parinthesis_begin_count++;
				else if (input[j] == ')')  parinthesis_end_count++;
				if (parinthesis_begin_count == parinthesis_end_count) {
					inputSize++;
					input.insert(j, ")");
					break;
				}
			}
		}
	}

	std::cout << "input: " << input << std::endl;
	for (unsigned i = 0; i < inputSize; i++) {


		//If the symbol is a number add it to the return value
		if (isNumber(input[i])) {
			std::string tmp = "";
			tmp.append(&input[i], 1);
			for (unsigned j = i + 1; j < inputSize; j++) {
				if (isNumber(input[j])) {
					tmp.append(&input[j], 1);
					i++;
				}
				else break;
			}
			result.append(tmp);
			result.append(" ");
		}

		//If the symbol is an operator
		else if (isOperator(input[i])) {
			
			//check if the - sign is followed by a number n. If it is, change it to 0-n.
			
			//1) as long as there is an operator at the top of the stack, o2 such that:

			//o1 is left associative and its order of execution is less than or equal to the order of o2,

			while (s.size() > 0 && isOperator(s.top()[0]) &&
				operatorOrder.at(std::string(&input[i], 1)) <= operatorOrder.at(s.top())) {

				//pop o2 off the stack and add it to the output queue and do again 1)
				result.append(s.top());
				result.append(" ");
				s.pop();
			}
			s.push(std::string(&input[i], 1));
		}
		//If the symbol is a left bracket add it to the stack
		else if (input[i] == '(') {
			s.push("(");
		}

		/*if the symbol is a right parenthesis then pop the operators off the stack and
		append them to the output queue, until the symbol at the top of the stack is a
		left parenthesis, when you get to that point, remove the left parenthesis from
		the stack without adding it to the output queue.
		*/

		else if (input[i] == ')') {
			while (s.top() != "(") {
				result.append(s.top());
				result.append(" ");
				s.pop();
			}
			if (s.top() == "(") s.pop();
		}
	}
	//Add all of the remaining operators to the result.
	while (!s.empty()) {
		result.append(s.top());
		result.append(" ");
		s.pop();
	}
	return result;
}

double rpn::calculateRPN(const std::string& str) {
	std::cout << "Calculating..." << std::endl;
	std::string input(str);
	double result = 0.0;
	std::replace(input.begin(), input.end(), 'x', '*'); //some people may like to use x instead of * to multiply
	std::replace(input.begin(), input.end(), ':', '/'); //same goes with :
	unsigned inputSize = input.length();
	std::stack<std::string> s;
	for (unsigned i = 0; i < inputSize; i++) {

		//if the symbol is a number, add it to the stack
		if (isNumber(input[i])) {
			std::string tmp = "";
			tmp.append(&input[i], 1);
			for (unsigned j = i + 1; j < inputSize; j++) {
				if (isNumber(input[j])) {
					tmp.append(&input[j], 1);
					i++;
				}
				else break;
			}
			s.push(tmp);
		}
		//if the symbol is an operator, perform the calculation of two previous numbers.
		else if (isOperator(input[i])) {
			double a = std::stod(s.top());
			s.pop();
			double b = std::stod(s.top());
			s.pop();

			s.push(std::to_string(calculate(a, b, input[i])));
		}
	}
	//save the result
	result = std::stod(s.top());
	s.pop();
	return result;
}
