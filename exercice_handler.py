import exercice_list
from tools import Tester, my_exec
from DB.db_utils import Result

BR = "<br>"


def getResultExercice(username, exercise_name, request_data):    
    success, logsExec = my_exec(request_data, None, locals())
    print("Log execution : " + logsExec)
    if success:
        method_to_call = getattr(exercice_list, exercise_name)
        try:
            copyArray = locals()
            result = method_to_call(logsExec, copyArray)
        except KeyError as keyError:
            return False, "KeyError (function not found?) : " + str(keyError)
        except Exception as err:
            return False, str(err)

    if success == False:
        return failHtml(logsExec)
    else:
        if isinstance(result, Tester):
            message, logs = result.results()

            resultSaved = Result.objects(username=username, exercise=exercise_name).first()
            if resultSaved is not None:
                resultSaved.solve = str(request_data)
                resultSaved.success = result.isWholeSuccess()
            else:
                resultSaved = Result(username=username, exercise=exercise_name, solve=request_data, success=result.isWholeSuccess())
            resultSaved.save()

            if resultSaved.success:
                return successHtml(message, logs)
            else:
                return noSuccessHtml(message, logs)
        else:
            return failHtml(result)



def successHtml(message, infos):
    infoValue = BR.join(infos)
    return "<div style='color: green;'>" + message + "<div style='text-size:10pt;'>" + infoValue + "</div></div>"

def noSuccessHtml(message, infos):
    infoValue = BR.join(infos)
    return "<div style='color: orange;'>" + message + "<div style='text-size:10pt;'>" + infoValue + "</div></div>"
    
def failHtml(message):
    return "<div style='color: red;'>" + message + "</div>"
