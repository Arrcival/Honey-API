from exercice_handler import getResultExercice


solving = """
def solve(x):
    return x * 3
y = 3
print(y - 1 + 66)
"""

result = getResultExercice("arrcival", "exercise1", solving)

print("Infos : %s" % result)