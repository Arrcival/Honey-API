import sys
from io import StringIO
import contextlib
import traceback

class Tester:
    solutions = 0
    questions = 0
    resultsArray = []
    def __init__(self):
        self.solutions = 0
        self.questions = 0
        self.resultsArray = []
    def test(self, assertBoolean, info=None):
        if assertBoolean:
            self.solutions += 1
        self.questions += 1
        if info is not None:
            self.resultsArray.append(info)
    def results(self):
        if self.isWholeSuccess():
            return f"Congratulations ! {self.questions} tests passed", self.resultsArray
        else:
            return f"{self.solutions} out of {self.questions} tests passed.", self.resultsArray
    def isWholeSuccess(self):
        return self.questions > 0 and self.solutions == self.questions
            
@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


def my_exec(cmd, globals=None, locals=None, description='source string'):
    with stdoutIO() as s:
        try:
            exec(cmd, globals, locals)
            return True, s.getvalue()
        except SyntaxError as err:
            error_class = err.__class__.__name__
            detail = err.args[0]
            line_number = err.lineno
            return False, f"Line {line_number} : {detail}"
        except Exception as err:
            error_class = err.__class__.__name__
            detail = err.args[0]
            cl, exc, tb = exc_info()
            line_number = traceback.extract_tb(tb)[-1][1]
            return False, f"Line {line_number} : {detail}"