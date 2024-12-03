import re

teststring = "asdasd"

doPattern = re.compile(r"do[(][)]")

print(re.findall(doPattern, teststring))
