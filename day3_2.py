import re

mulPattern = re.compile(r"mul[(]\d*,\d*[)]")
doPattern = re.compile(r"do[(][)]")
dontPattern = re.compile(r"don't[(][)]")
_listOfActiveSplits: list[str] = []
_bufferListOfSplits: list[str] = []
_listOfMatches: list[str] = []

with open("day3RawInput.txt", mode="r") as f:
    data = f.read()
    _bufferListOfSplits = re.split(dontPattern, data, maxsplit=1)

while _bufferListOfSplits[1] != "":
    _listOfActiveSplits.append(_bufferListOfSplits.pop(0))
    _bufferListOfSplits = re.split(doPattern, _bufferListOfSplits[0], maxsplit=1)
    if len(_bufferListOfSplits) == 1:
        break
    _bufferListOfSplits.pop(0)
    _bufferListOfSplits = re.split(dontPattern, _bufferListOfSplits[0], maxsplit=1)
    if len(_bufferListOfSplits) == 1:
        break

for split in _listOfActiveSplits:
    tempList = re.findall(mulPattern, split)
    if tempList:
        for match in tempList:
            _listOfMatches.append(match)


_mulCumulativeTotal: int = 0
for instruction in _listOfMatches:
    firstNumber, secondNumber = instruction[4:-1].split(",")
    _mulCumulativeTotal += int(firstNumber) * int(secondNumber)

print(_mulCumulativeTotal)
