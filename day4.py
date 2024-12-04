import re
from datetime import datetime

starttime = datetime.now()
with open("day4RawInput.txt", mode="r") as f:
    data = f.read()

_lol = data.find("\n")

#        N
#        |
#      \   /
#  W -   X   - E
#      /   \
#        |
#        S
_dictOfPatterns = {
    "nwPattern": re.compile(
        rf"(?=(S.{{{_lol+1}}}A.{{{_lol+1}}}M.{{{_lol+1}}}X))", re.DOTALL
    ),
    "nPattern": re.compile(rf"(?=(S.{{{_lol}}}A.{{{_lol}}}M.{{{_lol}}}X))", re.DOTALL),
    "nePattern": re.compile(
        rf"(?=(S.{{{_lol-1}}}A.{{{_lol-1}}}M.{{{_lol-1}}}X))", re.DOTALL
    ),
    "sePattern": re.compile(
        rf"(?=(X.{{{_lol+1}}}M.{{{_lol+1}}}A.{{{_lol+1}}}S))", re.DOTALL
    ),
    "sPattern": re.compile(rf"(?=(X.{{{_lol}}}M.{{{_lol}}}A.{{{_lol}}}S))", re.DOTALL),
    "swPattern": re.compile(
        rf"(?=(X.{{{_lol-1}}}M.{{{_lol-1}}}A.{{{_lol-1}}}S))", re.DOTALL
    ),
    "ePattern": re.compile(r"XMAS"),
    "wPattern": re.compile(r"SAMX"),
}

_occurencesOfXmas = 0
for pattern in _dictOfPatterns:
    matches = re.findall(_dictOfPatterns[pattern], data)
    _occurencesOfXmas += len(matches)

print(_occurencesOfXmas)
print(datetime.now() - starttime)
