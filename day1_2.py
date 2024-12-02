firstList: list[int] = []
secondList: list[int] = []

with open("day1RawInput.txt", mode="r") as f:
    for eachLine in f:
        firstListEntry, secondListEntry = eachLine.split("   ")
        firstList.append(int(firstListEntry))
        secondList.append(int(secondListEntry))

firstListSet = set(firstList)
occuranceFrequency: dict[int, int] = {eachEntry: 0 for eachEntry in firstListSet}

for eachEntry in secondList:
    if eachEntry in occuranceFrequency.keys():
        occuranceFrequency[eachEntry] += 1


similarityScore: list[int] = []
for eachKey in occuranceFrequency:
    similarityScore.append(eachKey * occuranceFrequency[eachKey])

print(sum(similarityScore))
