with open("day5TestInput.txt", mode="r") as f:
    data = f.read()

rules: str = data[: data.find("\n\n")]
ruleSet = set(rules.split("\n"))
updates: list[list[int]] = [
    [int(number) for number in eachUpdate.split(",")]
    for eachUpdate in data[data.find("\n\n") + 2 : -1].split("\n")
]


def getEachUpdateRelevantRuleSet(eachUpdate: list[int]) -> set:
    eachUpdateRuleSet = set()
    for eachPageNumber in eachUpdate:
        eachPageNumberRuleSet = set(
            [f"{str(eachPageNumber)}|{element}" for element in eachUpdate]
        )
        eachUpdateRuleSet = eachUpdateRuleSet | eachPageNumberRuleSet
    return eachUpdateRuleSet & ruleSet


def getMiddleValueIfIncorrect(eachUpdate: list[int]):
    comparisonList = eachUpdate.copy()
    eachUpdateRuleSet = getEachUpdateRelevantRuleSet(eachUpdate)
    print(eachUpdateRuleSet)
    for eachRule in eachUpdateRuleSet:
        firstNumber, secondNumber = eachRule.split("|")
        if eachUpdate.index(int(firstNumber)) > eachUpdate.index(int(secondNumber)):
            (
                eachUpdate[eachUpdate.index(int(firstNumber))],
                eachUpdate[eachUpdate.index(int(secondNumber))],
            ) = (
                eachUpdate[eachUpdate.index(int(secondNumber))],
                eachUpdate[eachUpdate.index(int(firstNumber))],
            )

    if comparisonList != eachUpdate:
        return int(eachUpdate[int((len(eachUpdate) - 1) / 2)])
    else:
        return 0


totalMiddlePageNumberValue = 0
for eachUpdate in updates:
    totalMiddlePageNumberValue += getMiddleValueIfIncorrect(eachUpdate)

print(totalMiddlePageNumberValue)
