class Problem(object):

  def __init__(self, probString):
    self.problemString = probString
    self.operandOne = None
    self.operandTwo = None
    self.operator = None
    self.longestOperandLength = None
    self.answer = None

  def parseProblemString(self):
    unpackable = self.problemString.split(' ')
    if len(unpackable) != 3:
      return "Error: Each problem should have two operands and an operator in infix notation."
    self.operandOne, self.operator, self.operandTwo = unpackable
    try:
      self.operandOne = int(self.operandOne)
      self.operandTwo = int(self.operandTwo)
    except:
      return "Error: Numbers must only contain digits."
    if not self.checkOperatorSupport():
      return "Error: Operator must be '+' or '-'."
    if not self.checkOperandLength():
      return "Error: Numbers cannot be more than four digits."
    return None

  def checkOperatorSupport(self):
    if self.operator in ['+', '-']:
      return True
    return False

  def checkOperandLength(self):
    if self.getLongestOperandLength() > 4:
      return False
    return True

  def getLongestOperandLength(self):
    self.longestOperandLength = max([len(str(self.operandOne)), len(str(self.operandTwo))])
    return self.longestOperandLength

  def solveProblem(self):
    self.answer = eval(self.problemString)

  def formatProblem(self, solve=False):
    lineLength = self.longestOperandLength + 2
    self.formattedLines = []
    self.formattedLines.append(str(self.operandOne).rjust(lineLength))
    self.formattedLines.append(self.operator + str(self.operandTwo).rjust(lineLength - 1))
    self.formattedLines.append("-" * lineLength)
    if solve:
      self.solveProblem()
      self.formattedLines.append(str(self.answer).rjust(lineLength))