#include <iostream>
#include <string>
#include <stack>
#include <vector>
#include <iterator>
#include <map>
#include <exception>
#include <cmath>
#include <algorithm>

const std::vector<char> digits = { '0','1','2','3','4','5','6','7','8','9' };
const std::vector<char> operators = { '+','-','*','/','^' };
const std::map<std::string, unsigned> operatorOrder = { {"+",1},{"-",1},{"*",2},{"/",2},{"^",3}};
bool isNumber(const char input) {
	return input >= 48 && input <= 57;
}

bool isOperator(const char value) {
	return std::find(operators.begin(), operators.end(), value) != operators.end();
}

double calculate(const double a, const double b, const char op) {
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
std::string convertToRPN(std::string& input)
{	
	std::string result = "";
	std::stack<std::string> s;
	unsigned inputSize = input.length();

	input.erase(std::remove(input.begin(), input.end(), ' '), input.end());
	std::cout << input << std::endl;
	std::replace(input.begin(), input.end(), 'x', '*'); //some people may like to use x instead of * to multiply
	std::replace(input.begin(), input.end(), ':', '/'); //same goes with :
	for(unsigned i=0; i<inputSize; i++){
		std::cout << "iteracja: " << i << std::endl;


		//jezeli symbol jest liczbą dodaj go do wyjscia
		if (isNumber(input[i])) {
			std::cout << "wykryto cyfre: " << input[i] << std::endl;
			std::string tmp = "";
			tmp.append(&input[i], 1);
			for (unsigned j = i + 1; j < inputSize; j++) {
				if (isNumber(input[j])) {
					tmp.append(&input[j], 1);
					i++;
					std::cout << "wykryto cyfre: " << input[j] << std::endl;
				}
				else break;
			}
			std::cout << "dodano liczbe: " << tmp << " do wyjscia"<<std::endl;
			result.append(tmp);
			result.append(" ");
		}

		//jezeli symbol jest operatorem
		else if (isOperator(input[i])) {
			std::cout << "wykryto operator: " << input[i] << std::endl;
			//1) dopóki na górze stosu znajduje się operator, o2 taki, że:
			//
            //o1 jest lewostronnie łączny i jego kolejność wykonywania jest mniejsza lub równa kolejności wyk. o2,

			while (s.size()>0 && isOperator(s.top()[0]) &&
				operatorOrder.at(std::string(&input[i],1)) <= operatorOrder.at(s.top())) {
				//zdejmij o2 ze stosu i doloz go do kolejki wyjsciowej i powtorz jeszcze raz 1)
				result.append(s.top());
				result.append(" ");
				std::cout << "dodano " << s.top() << " do wyjscia" << std::endl;
				std::cout << "usunieto " << s.top() << " ze stosu" << std::endl;
				s.pop();
			}
			//2)
			//włóż o1 na stos operatorów.
			s.push(std::string(&input[i],1));
			std::cout << "dodano " << std::string(&input[i],1) << " do stosu" << std::endl;
		}
		//jezeli symbol jest lewym nawiasem wloz go na stos
		else if (input[i] == '(') {
			std::cout << "Wykryto nawias lewy" << std::endl;
			s.push("("); }

		//Jeżeli symbol jest prawym nawiasem to zdejmuj operatory
		//ze stosu i dokładaj je do kolejki wyjście, dopóki
		//symbol na górze stosu nie jest lewym nawiasem,
		//kiedy dojdziesz do tego miejsca zdejmij lewy nawias
		//ze stosu bez dokładania go do kolejki wyjście.
		else if (input[i] == ')') {
			while (s.top() != "(") {
				result.append(s.top());
				result.append(" ");
				s.pop();
			}
			if (s.top() == "(") s.pop();
		}
	}
	while (!s.empty()) {
		result.append(s.top());
		result.append(" ");
		s.pop();
	}
	//
	return result;
}


double calculateRPN(const std::string& input) {
	double result = 0.0;
	unsigned inputSize= input.length();
	std::stack<std::string> s;

	for (unsigned i = 0; i < inputSize; i++) {


		if (isNumber(input[i])) {
			std::cout << "wykryto cyfre: " << input[i] << std::endl;
			std::string tmp = "";
			tmp.append(&input[i], 1);
			for (unsigned j = i + 1; j < inputSize; j++) {
				if (isNumber(input[j])) {
					tmp.append(&input[j], 1);
					i++;
					std::cout << "wykryto cyfre: " << input[j] << std::endl;
				}
				else break;
			}
			s.push(tmp);
		}

		if (isOperator(input[i])) {
			double a = std::stod(s.top());
			s.pop();
			double b = std::stod(s.top());
			s.pop();

			s.push(std::to_string(calculate(a, b, input[i])));
		}
	}
	result = std::stod(s.top());
	s.pop();
	return result;
}
int main() {
	std::string dzialanie;
	std::cout << "Podaj dzialanie: "<<std::endl;
	std::getline(std::cin, dzialanie);
	auto rpn = convertToRPN(dzialanie);
	std::cout << "Odwrotna notacja polska: " << rpn << std::endl;
	double wynik = calculateRPN(rpn);
	std::cout << "Wynik dzialania: " << wynik;
	return 0;
}