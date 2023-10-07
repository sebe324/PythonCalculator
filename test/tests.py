import MyMathLibrary as mml

tests_amount = 0
tests_passed = 0
def rpnTest(equationInfix, expectedResult):
    global tests_amount
    global tests_passed
    tests_amount+=1
    print("Begin test")
    print("Testing sample: ", equationInfix)
    equationrpn=mml.convertToRPN(equationInfix)
    print("Conversion: ", equationrpn)
    result = mml.calculateRPN(equationrpn)
    print("Calculation result", result)
    print("Expected result", expectedResult)
    if(result==expectedResult):
        print("-------","TEST PASSED","-------",sep='\n')
        tests_passed+=1
        return True
    elif(abs(result-expectedResult)<=0.001):
        print("Small Difference, probably caused by finite precision")
        print("-------","TEST PASSED","-------",sep='\n')
        tests_passed+=1
        return True
    else:
        print("-------","TEST FAILED","-------",sep='\n')
        return False

pi = "3.14159265359"
mml.setUseRadians(True)
rpnTest("3 + 2 * 5", 13.0)
rpnTest("2 * (5 + 2)", 14.0)
rpnTest("(7 + 3) * (5 - 2) ^ 2", 90.0)
rpnTest("4 / (3 - 1) ^ (2 * 3) ", 0.0625)
rpnTest("( ( 5 - 2 ) ^ ( 3 + 1 ) / ( 2 + 1 ) + 12 ) * 21.0", 819.0)
rpnTest("sin(0.523599)", 0.5)
rpnTest("4^3^2", 262144)
rpnTest("sin(30*"+pi+"/180)+2", 2.5)
rpnTest("cos(60*"+pi+"/180)^2", 0.25)
rpnTest("cos()", 0.0)
rpnTest("cos(30*3.14159265359/180)^2+sin(30*3.14159265359/180)^2", 1)
rpnTest("tg(45*"+pi+"/180)",1)
rpnTest("abs(30-100)*3",210)
rpnTest("abs(-5)*-20",-100)
rpnTest("abs(30-100)*abs(-3)",210)
mml.setUseRadians(False)
rpnTest("sin(30)",0.5)
print("FINAL RESULT",tests_passed,"/",tests_amount)