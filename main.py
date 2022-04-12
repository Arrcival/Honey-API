import flask
from flask import request
from flask_cors import CORS
from exercice_handler import getResultExercice
from DB.db_utils import Result, checkRequest
from mongoengine.connection import disconnect
import atexit
import codecs
import os

app = flask.Flask(__name__)
CORS(app)

@app.route('/ping', methods=['GET'])
def indexRoute():
    return "Pong !"

@app.route('/getAmountExercises/<username>', methods=['GET'])
def getAmountExercices(username):
    if not checkRequest(request):
        return "Not authorized", 401
    return str(Result.objects(username=username, success=True).count())

@app.route('/exercise/<exerciseName>/<username>', methods=['POST'])
def sendExercise(exerciseName, username):
    if not checkRequest(request):
        return "Not authorized", 401
    request_data = request.get_data().decode("utf-8")
    return getResultExercice(username, exerciseName, request_data)

@app.route('/getResultsExercise/<username>', methods=['GET'])
def getResultsExercise(username):
    if not checkRequest(request):
        return "Not authorized", 401
    results = Result.objects(username=username)
    if results is None:
        return ""
    returnString = ""
    for result in results:
        returnString += f"{result.exercise}/{str(2) if result.success else str(1)}\n"
    return returnString

@app.route('/getExercise/<exerciseName>', methods=['GET'])
def getExercise(exerciseName):
    if not checkRequest(request):
        return "Not authorized", 401
    dirName = os.path.dirname(os.path.realpath(__file__))
    pathFile = os.path.join(f"{dirName}", "exercises", f"{exerciseName}.html")
    if not os.path.exists(pathFile):
        print("path not found")
        return ""
    file = codecs.open(pathFile, "r", "utf-8")
    return file.read()

@app.route('/getExerciseResult/<exerciseName>/<username>', methods=['GET'])
def getExerciseResult(exerciseName, username):
    if not checkRequest(request):
        return "Not authorized", 401
    result = Result.objects(username=username, exercise=exerciseName).first()
    if result is not None:
        return str(result.success) + "\n" + result.solve
    return ""

@app.route('/getBooleanExerciseResult/<exerciseName>/<username>', methods=['GET'])
def getBooleanExerciseResult(exerciseName, username):
    if not checkRequest(request):
        return "Not authorized", 401
    result = Result.objects(username=username, exercise=exerciseName).first()
    if result is not None:
        return f"{str(2) if result.success else str(1)}"
    return str(0)

def onExit():
    disconnect()
    print("Gracefully closed.")

atexit.register(onExit)

if __name__ == '__main__':
    app.run()

