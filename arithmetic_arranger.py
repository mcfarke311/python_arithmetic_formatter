from problem import Problem
def arithmetic_arranger(problems, solve=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  formattedProblems = []
  for problem in problems:
    p = Problem(problem)
    returnString = p.parseProblemString()
    if returnString:
      return returnString
    p.formatProblem(solve)
    formattedProblems.append(p)

  numProblems = len(formattedProblems)
  numLines = len(p.formattedLines)
  finalStrings = []
  for i in range(numLines):
    for j in range(numProblems):
      finalStrings.append(formattedProblems[j].formattedLines[i])
      if j != (numProblems - 1):
        finalStrings.append(' ' * 4)
      else:
        if i != (numLines - 1):
          finalStrings.append('\n')

  final = ''.join(finalStrings)
  print(finalStrings)
  print(final)
  return final

  return None