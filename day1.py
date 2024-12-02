import json

firstList: list[int] = []
secondList: list[int] = []

with open("day1RawInput.txt", mode="r") as f:
    for eachLine in f:
        firstListEntry, secondListEntry = eachLine.split("   ")
        firstList.append(int(firstListEntry))
        secondList.append(int(secondListEntry))

firstList.sort()
secondList.sort()

distanceList: list[int] = []

for i in range(len(firstList)):
    distanceList.append(abs(firstList[i] - secondList[i]))

print(sum(distanceList))
