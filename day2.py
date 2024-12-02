reportsList: list[list[int]] = []

with open("day2RawInput.txt", mode="r") as f:
    for eachReport in f:
        reportsList.append(eachReport.split())


def isValidReport(eachReport: list) -> bool:
    diffList: list[int] = []
    for index in range(len(eachReport) - 1):
        diffList.append(int(eachReport[index]) - int(eachReport[index + 1]))

    negativeFlag: bool = False
    if diffList[0] < 0:
        negativeFlag: bool = True

    for eachNumber in diffList:
        if negativeFlag and (eachNumber > 0):
            return False

        if (not negativeFlag) and (eachNumber < 0):
            return False

        if abs(eachNumber) > 3 or abs(eachNumber) < 1:
            return False

    return True


_validCounter: int = 0
for eachReport in reportsList:
    if isValidReport(eachReport):
        _validCounter += 1

print(_validCounter)
