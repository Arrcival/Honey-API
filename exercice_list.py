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