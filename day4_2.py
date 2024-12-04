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
_dictOfXPatterns = {
    "mmPattern": re.compile(
        rf"(?=(M.{{{1}}}M.{{{_lol-1}}}A.{{{_lol-1}}}S.{{{1}}}S))", re.DOTALL
    ),
    "ssPattern": re.compile(
        rf"(?=(S.{{{1}}}S.{{{_lol-1}}}A.{{{_lol-1}}}M.{{{1}}}M))", re.DOTALL
    ),
    "msPattern": re.compile(
        rf"(?=(M.{{{1}}}S.{{{_lol-1}}}A.{{{_lol-1}}}M.{{{1}}}S))", re.DOTALL
    ),
    "smPattern": re.compile(
        rf"(?=(S.{{{1}}}M.{{{_lol-1}}}A.{{{_lol-1}}}S.{{{1}}}M))", re.DOTALL
    ),
}

_occurencesOfXmas = 0
for pattern in _dictOfXPatterns:
    matches = re.findall(_dictOfXPatterns[pattern], data)
    _occurencesOfXmas += len(matches)

print(_occurencesOfXmas)
print(datetime.now() - starttime)
