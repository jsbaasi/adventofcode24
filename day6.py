# importing the sys module
import sys

# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs
sys.setrecursionlimit(10**8)


class Solution:
    def part1(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        dirs = {
            "v": (1, 0),
            "^": (-1, 0),
            ">": (0, 1),
            "<": (0, -1),
        }
        alter: dict[tuple] = {
            (-1, 0): (1, 1),
            (0, 1): (1, -1),
            (1, 0): (-1, -1),
            (0, -1): (-1, 1),
        }
        turn: dict[tuple] = {
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1),
            (0, 1): (1, 0),
        }
        res = 1

        def dfs(r, c, dir: tuple):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            if grid[r][c] == "#":
                alteration = alter[dir]
                newDir = turn[dir]
                dfs(
                    r + alteration[0],
                    c + alteration[1],
                    newDir,
                )
                return
            if grid[r][c] == ".":
                nonlocal res
                res += 1
                s = grid[r][:c] + "X" + grid[r][c + 1 :]
                grid[r] = s
            dfs(
                r + dir[0],
                c + dir[1],
                dir,
            )
            return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] in dirs:
                    dfs(r, c, dirs[grid[r][c]])

        return res

    def part2(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        dirs = {
            "v": (1, 0),
            "^": (-1, 0),
            ">": (0, 1),
            "<": (0, -1),
        }
        alter: dict[tuple] = {
            (-1, 0): (1, 1),
            (0, 1): (1, -1),
            (1, 0): (-1, -1),
            (0, -1): (-1, 1),
        }
        turn: dict[tuple] = {
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1),
            (0, 1): (1, 0),
        }

        upSet = set()
        downSet = set()
        rightSet = set()
        leftSet = set()

        dictOfSets = {
            (1, 0): downSet,
            (-1, 0): upSet,
            (0, 1): rightSet,
            (0, -1): leftSet,
        }
        res = 0

        def dfs(r, c, dir: tuple):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            if grid[r][c] == ".":
                s = grid[r][:c] + "," + grid[r][c + 1 :]
                grid[r] = s
                dictOfSets[dir].add((r, c))
            turnDir = turn[dir]
            if (0 <= r + turnDir[0] < ROWS) and (0 <= c + turnDir[1] < COLS):
                toMyRight = (r + turnDir[0], c + turnDir[1])
                toMyRightGrid = grid[r + turnDir[0]][c + turnDir[1]]
                if toMyRightGrid == ",":
                    if toMyRight in dictOfSets[turnDir]:
                        nonlocal res
                        res += 1
            if (0 <= r + dir[0] < ROWS) and (0 <= c + dir[1] < COLS):
                if grid[r + dir[0]][c + dir[1]] == "#":
                    dfs(
                        r + turnDir[0],
                        c + turnDir[1],
                        turnDir,
                    )
            dfs(
                r + dir[0],
                c + dir[1],
                dir,
            )

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] in dirs:
                    dir = dirs[grid[r][c]]
                    s = grid[r][:c] + "," + grid[r][c + 1 :]
                    grid[r] = s
                    upSet.add((r, c))
                    dfs(r, c, dir)
                    return res


grid = []
with open("day6TestInput.txt") as f:
    for line in f:
        grid.append(line.rstrip())

obj = Solution()
print(obj.part1(grid))
# print(obj.part2(grid))
