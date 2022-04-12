import sys
import traceback

def my_exec(cmd, globals=None, locals=None, description='source string'):
    try:
        return exec(cmd, globals, locals)
    except SyntaxError as err:
        error_class = err.__class__.__name__
        detail = err.args[0]
        line_number = err.lineno
        return ("Line %i : %s" % (line_number, detail))
    except Exception as err:
        error_class = err.__class__.__name__
        detail = err.args[0]
        cl, exc, tb = sys.exc_info()
        line_number = traceback.extract_tb(tb)[-1][1]
        return ("Line %i : %s" % (line_number, detail))
        

globalsParameter = {'__builtins__' : None}
localsParameter = {'print': print}

def testingPurposes(x):
    print("Fonction non-implémentée")

input_code = """
def testingPurposes(x):
    x = x + 2
    print("X : " + str(x))
"""

my_exec(input_code, None, locals())


def exerciceOne():
    try:
        testingPurposes(2)
        return True
    except Exception as err:
        print(err.args[0])
        return False

print(exerciceOne())


