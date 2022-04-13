from tools import my_exec, Tester, stdoutIO

def exercise1(logs, localMethods):
    #print("my_exec result : " + result)
    tester = Tester()
    #arr = locals()
    #rtr = arr["solve"]
    #result = rtr.__call__(3)
    firstPrint = logs.split("\n")[0]
    tester.test("1" == firstPrint, f"Waiting for : 1 / Got : {firstPrint}")
    return tester

def exercise2(logs, localMethods):
    tester = Tester()
    firstPrint = logs.split("\n")[0]
    tester.test("I like honey" == firstPrint, f"Waiting for : \"I like honey\" / Got : {firstPrint}")
    return tester

def exercise3(logs, localMethods):
    tester = Tester()
    firstPrint = logs.split("\n")[0]
    tester.test(str(6198 * 37) == firstPrint, f"Waiting for : {str(6198 * 37)} / Got : {firstPrint}")
    return tester

def exercise4(logs, localMethods):
    tester = Tester()
    firstPrint = logs.split("\n")[0]
    tester.test(str(99) == firstPrint, f"Waiting for : 99 / Got : {firstPrint}")
    return tester

def exercise5(logs, localMethods):
    tester = Tester()
    firstPrint = logs.split("\n")[0]
    tester.test(str(20) == firstPrint, f"Waiting for : 20 / Got : {firstPrint}")
    return tester

def exercise6(logs, localMethods):
    tester = Tester()
    firstPrint = logs.split("\n")[0]
    tester.test("Function called" == firstPrint, f"Waiting for : Function called / Got : {firstPrint}")
    return tester

def exercise7(logs, localMethods):
    tester = Tester()
    rtr = localMethods["function"]
    with stdoutIO() as s:
        result = rtr.__call__()
    printValue = s.getvalue().split("\n")[0]
    tester.test("Function tested" == printValue, f"Waiting for : Function tested / Got : {printValue}")
    return tester

def exercise8(logs, localMethods):
    tester = Tester()
    firstPrint = logs.split("\n")[0]
    tester.test("5" == firstPrint, f"Waiting for : 5 / Got : {firstPrint}")
    return tester

def exercise9(logs, localMethods):
    tester = Tester()
    firstPrint = logs.split("\n")[0]
    tester.test("34348" == firstPrint, f"Waiting for : 34348 / Got : {firstPrint}")
    return tester

def exercise10(logs, localMethods):
    tester = Tester()
    rtr = localMethods["cube"]
    result1 = rtr.__call__(2)
    result2 = rtr.__call__(3)
    result3 = rtr.__call__(5)
    tester.test("8" == result1, f"Waiting for : 8 / Got : {result1}")
    tester.test("27" == result2, f"Waiting for : 27 / Got : {result2}")
    tester.test("125" == result2, f"Waiting for : 125 / Got : {result3}")
    return tester

def exercise11(logs, localMethods):
    tester = Tester()
    rtr = localMethods["printIfTrue"]
    with stdoutIO() as s:
        result = rtr.__call__("Should be displayed", True)
    printValue = s.getvalue().split("\n")[0]
    tester.test("Should be displayed" == printValue, f"Waiting for : Should be displayed / Got : {printValue}")
    with stdoutIO() as s:
        result = rtr.__call__("Should not be displayed", False)
    printValue = s.getvalue().split("\n")[0]
    tester.test("" == printValue, f"Waiting for : / Got : {printValue}")
    return tester

def exercise12(logs, localMethods):
    tester = Tester()
    rtr = localMethods["specialMaths"]
    result = rtr.__call__(10, True)
    tester.test(11 == result, f"Waiting for : 11/ Got : {result}")
    result = rtr.__call__(10, False)
    tester.test(9 == result, f"Waiting for : 9 / Got : {result}")
    return tester

def exercise13(logs, localMethods):
    tester = Tester()
    rtr = localMethods["printIfEquals"]
    with stdoutIO() as s:
        result = rtr.__call__(15, 15)
    printValue = s.getvalue().split("\n")[0]
    tester.test("They are equals" == printValue, f"Waiting for : They are equals / Got : {printValue}")
    with stdoutIO() as s:
        result = rtr.__call__(10, 11)
    printValue = s.getvalue().split("\n")[0]
    tester.test("" == printValue, f"Waiting for : / Got : {printValue}")
    return tester