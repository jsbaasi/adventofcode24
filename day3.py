import re

myPattern = re.compile(r"mul[(]\d*,\d*[)]")
listOfMatches: list[str] = []

with open("day3RawInput.txt", mode="r") as f:
    data = f.read()
    listOfMatches = re.findall(myPattern, data)

mulCumulativeTotal = 0
for instruction in listOfMatches:
    firstNumber, secondNumber = instruction[4:-1].split(",")
    mulCumulativeTotal += int(firstNumber) * int(secondNumber)

print(mulCumulativeTotal)
