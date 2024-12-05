with open("day5TestInput.txt", mode="r") as f:
    data = f.read()

rules: str = data[: data.find("\n\n")]
updates: list[list[int]] = [
    [int(number) for number in eachUpdate.split(",")]
    for eachUpdate in data[data.find("\n\n") + 2 : -1].split("\n")
]

ruleSet = set(rules.split("\n"))


def getMiddleValueIfIncorrect(eachUpdate: list[int]):
    eachUpdateRuleSet = set()
    swappedNumber = False
    checkingList = eachUpdate.copy()

    for eachPageNumber in eachUpdate:
        eachPageNumberRuleSet = set(
            [f"{str(eachPageNumber)}|{element}" for element in eachUpdate]
        )
        eachUpdateRuleSet = eachUpdateRuleSet | eachPageNumberRuleSet
    eachUpdateRuleSet = eachUpdateRuleSet & ruleSet
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
    if checkingList != eachUpdate:
        return int(eachUpdate[int((len(eachUpdate) - 1) / 2)])
    return 0


totalMiddlePageNumberValue = 0
for eachUpdate in updates:
    totalMiddlePageNumberValue += getMiddleValueIfIncorrect(eachUpdate)

print(totalMiddlePageNumberValue)
