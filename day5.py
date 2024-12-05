with open("day5RawInput.txt", mode="r") as f:
    data = f.read()

rules: str = data[: data.find("\n\n")]
updates: list[list[int]] = [
    [int(number) for number in eachUpdate.split(",")]
    for eachUpdate in data[data.find("\n\n") + 2 : -1].split("\n")
]

ruleSet = set(rules.split("\n"))


def checkEachUpdate(eachUpdate):
    eachUpdateRuleSet = set()

    for eachPageNumber in eachUpdate:
        eachPageNumberRuleSet = set(
            [f"{str(eachPageNumber)}|{element}" for element in eachUpdate]
        )
        eachUpdateRuleSet = eachUpdateRuleSet | eachPageNumberRuleSet
    eachUpdateRuleSet = eachUpdateRuleSet & ruleSet
    for eachRule in eachUpdateRuleSet:
        firstNumber, secondNumber = eachRule.split("|")
        if eachUpdate.index(int(firstNumber)) > eachUpdate.index(int(secondNumber)):
            return False
    return True


totalMiddlePageNumberValue = 0
for eachUpdate in updates:
    if not checkEachUpdate(eachUpdate):
        continue
    totalMiddlePageNumberValue += int(eachUpdate[int((len(eachUpdate) - 1) / 2)])

print(totalMiddlePageNumberValue)
